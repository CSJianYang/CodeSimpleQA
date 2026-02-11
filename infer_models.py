from utils import utils
import argparse
import transformers
import tqdm
from tqdm.asyncio import tqdm_asyncio
import asyncio
import os
import prompts
def parse_args():
    parser = argparse.ArgumentParser(description='Parameters')
    parser.add_argument("--model", "-model", default="Qwen2.5-Coder-32B-Instruct", type=str, help="model path")
    parser.add_argument("--use_api", "-use_api", action="store_true", help="model path")
    parser.add_argument("--input_path", "-input_path", default="./CodeSimpleQA/data/test_data/code_simpleqa_eval_2k.jsonl", type=str, help="")
    parser.add_argument("--output_path", "-output_path", default="./CodeSimpleQA/data/eval_results/Qwen2.5-Coder-32B-Instruct/code_simpleqa_eval_2k.jsonl", type=str, help="")
    parser.add_argument("--cache_dir", "-cache_dir", default="./CodeSimpleQA/data/eval_results/Qwen2.5-Coder-32B-Instruct/cache/", type=str, help="")
    parser.add_argument("--max_tokens", "-max_tokens", default=8192 * 2, type=int, help="")
    parser.add_argument("--workers", "-workers", default = 1, type=int, help="")
    parser.add_argument("--chunk_size", "-chunk_size", default = 5, type=int, help="")
    parser.add_argument("--temperature", "-temperature", default = 1.0, type=float, help="")
    parser.add_argument("--top_p", "-top_p", default = 0.95, type=float, help="")
    parser.add_argument("--n", "-n", default = 1, type=int, help="")
    parser.add_argument("--enable_thinking", "-enable_thinking", action="store_true", help="model path")
    parser.add_argument("--chat_template", "-chat_template", default="auto", type=str, choices=["auto", "codellama"], help="")
    parser.add_argument("--base_url", "-base_url", default="", type=str, help="") #
    parser.add_argument("--api_key", "-api_key", default="sk-abc123", type=str, help="") #
    parser.add_argument("--progress", "-progress", type=bool, default=True)
    parser.add_argument("--tensor_parallel_size", "-tensor_parallel_size", default=1, type=int, help="")
    parser.add_argument("--prompt_template", "-prompt_template", default="normal", choices = ["normal", "calibration"], type=str, help="")
    args = parser.parse_args()
    return args


def load_cache_data(objs, cache_dir):
    left_objs = []
    cached_objs = []
    for uid, obj in tqdm.tqdm(enumerate(objs)):
        obj["uid"] = uid
        cache_path = os.path.join(cache_dir, f"{uid}.json")
        if os.path.exists(cache_path):
            obj = utils.read_json(cache_path)
            cached_objs.append(obj)
        else:
            left_objs.append(obj)
    print(f"Successfully loaded {len(cached_objs)} cached objs")
    print(f"Left {len(left_objs)} objs to process")
    return left_objs, cached_objs


async def async_start_llm_judgement(obj, args):
    if args.prompt_template == "normal":
        if obj["human_language"] == "chinese":
            prompt = obj["question"] + "\n" + "回复不要超过64个单词"
        else:
            prompt = obj["question"] + "\n" + "Response should not exceed 64 words"
    else:
        if obj["human_language"] == "chinese":
            prompt = prompts.calibration_zh_prompt.format_map({"question": obj["question"]})
        else:
            prompt = prompts.calibration_en_prompt.format_map({"question": obj["question"]})
    #
    openai_args = {
        "model": args.model,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "n": args.n,
        "top_p": args.top_p,
        "messages": [{"role": "user", "content": prompt}],
    }
    obj["response"] = await utils.async_chat(base_url = args.base_url, api_key = args.api_key, **openai_args)
    obj["model"] = args.model
    utils.save_json(obj, os.path.join(args.cache_dir, f"{obj['uid']}.json"), logging = False)
    return obj


async def async_start_llm_judgements(objs, args):
    async def limited_task(obj, semaphore):
        async with semaphore:  # This will limit concurrent executions
            return await async_start_llm_judgement(obj, args)
    
    semaphore = asyncio.Semaphore(args.workers)
    tasks = [limited_task(obj, semaphore) for obj in objs]
    if args.progress:
        objs = await tqdm_asyncio.gather(*tasks, desc="Processing")
    else:
        objs = await asyncio.gather(*tasks)
    return objs


def main():
    args = parse_args()
    print(args)
    os.makedirs(args.cache_dir, exist_ok=True)
    print(args)
    test_data = utils.read_jsonl_file(args.input_path, max_sentence=None)
    if args.use_api:
        os.makedirs(os.path.dirname(args.output_path), exist_ok = True)
        left_objs, cached_objs = load_cache_data(test_data, args.cache_dir)
        left_objs = asyncio.run(async_start_llm_judgements(left_objs, args))
        data = left_objs + cached_objs
        data.sort(key=lambda x: x["uid"])
    else:
        import vllm
        tokenizer = transformers.AutoTokenizer.from_pretrained(args.model, trust_remote_code = True)
        if hasattr(tokenizer, "model_max_length"):
            args.model_max_len = args.model_max_len if tokenizer.model_max_length > args.model_max_len else tokenizer.model_max_length
            print(f"max_length: {tokenizer.model_max_length}, cur_length: {args.model_max_len}")
        print(f"Model Max Length: {args.model_max_len}")
        for obj in tqdm.tqdm(data):
            if args.chat_template == "codellama":
                codellama_template = "<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{instruction} [/INST]"
                obj["input"] = codellama_template.format_map({"system_prompt": "", "instruction": obj["messages"][-1]["content"]})
            else:
                if "qwen3" in args.model:
                    obj["input"] = tokenizer.apply_chat_template(obj["messages"], add_generation_prompt = True, tokenize = False, enable_thinking = args.enable_thinking)
                else:
                    obj["input"] = tokenizer.apply_chat_template(obj["messages"], add_generation_prompt = True, tokenize = False)
        print("*****template*******")
        print(data[0]["input"])
        print("*****template*******")
        sampling_params = vllm.SamplingParams(temperature = 0.0, top_p = 0.95, max_tokens = args.model_max_len)
        model = vllm.LLM(
            model = args.model, tensor_parallel_size = args.tensor_parallel_size, # gpu_memory_utilization=0.95,
            trust_remote_code = True, max_model_len = args.model_max_len #worker_use_ray=True, 
        )
        prompts = [obj["input"] for obj in data]
        outputs = model.generate(prompts, sampling_params)
        for obj, o in zip(data, outputs):
            obj["model"] = args.model
            obj["response"] = o.outputs[0].text
    utils.write_jsonl_file(data, args.output_path)

if __name__ == "__main__":
    main()

    


