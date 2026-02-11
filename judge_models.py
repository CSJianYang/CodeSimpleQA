from utils import utils
import argparse
import pandas as pd
import tqdm
from tqdm.asyncio import tqdm_asyncio
import asyncio
import os
import prompts
import re
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", "-input_path", type=str, default="./CodeSimpleQA/data/eval_results/Qwen2.5-Coder-32B-Instruct/code_simpleqa_eval_2k.jsonl")
    parser.add_argument("--output_path", "-output_path", type=str, default="./CodeSimpleQA/data/eval_results/Qwen2.5-Coder-32B-Instruct/code_simpleqa_eval_2k.jsonl.judge")
    parser.add_argument("--cache_dir", "-cache_dir", type=str, default="./CodeSimpleQA/data/eval_results/Qwen2.5-Coder-32B-Instruct/judge_cache/")
    parser.add_argument("--base_url", "-base_url", type=str, default="") 
    parser.add_argument("--workers", "-workers", type=int, default = 1)
    parser.add_argument("--api_key", "-api_key", type=str, default="sk-abc123")
    parser.add_argument("--judge_model", "-judge_model", type=str, default="Qwen3-Coder-30B")
    parser.add_argument("--temperature", "-temperature", type=float, default = 0.0)
    parser.add_argument("--max_tokens", "-max_tokens", type=float, default = 32768)
    parser.add_argument("--judgement_only", "-judgement_only", action = "store_true")
    parser.add_argument("--evaluation_only", "-evaluation_only", action = "store_true")
    parser.add_argument("--progress", "-progress", type=bool, default=True)
    args = parser.parse_args()
    return args

def calculate_accuracies(group):
    if not isinstance(group, pd.DataFrame):
        group = pd.DataFrame(group)
    total_questions = len(group)
    total_correct = group[group['score'] == "A"].shape[0]
    total_incorrect = group[group['score'] == "B"].shape[0]
    total_not_attempted = group[group['score'] == "C"].shape[0]
    assert total_correct + total_incorrect + total_not_attempted == total_questions

    total_correct_accuracy = total_correct / total_questions if total_questions > 0 else 0
    total_incorrect_accuracy = total_incorrect / total_questions if total_questions > 0 else 0
    total_not_attempted_accuracy = total_not_attempted / total_questions if total_questions > 0 else 0
    total_given_attempted_accuracy = total_correct / (total_correct + total_incorrect) if (total_correct + total_incorrect) > 0 else 0
    f1 = 2 * total_given_attempted_accuracy * total_correct_accuracy / (total_given_attempted_accuracy+ total_correct_accuracy) if (total_given_attempted_accuracy+ total_correct_accuracy) > 0 else 0

    total_correct_accuracy = round(total_correct_accuracy, 3)
    total_incorrect_accuracy = round(total_incorrect_accuracy, 3)
    total_not_attempted_accuracy = round(total_not_attempted_accuracy, 3)
    total_given_attempted_accuracy = round(total_given_attempted_accuracy, 3)
    f1 = round(f1, 3)
    return {'correct': total_correct_accuracy, 'incorrect': total_incorrect_accuracy, 'not_attempted': total_not_attempted_accuracy, "given_attempted_accuracy": total_given_attempted_accuracy, "F1": f1}

def caculate_accuracies_by_domains(df):
    domain_accuracies = {}
    df["main_domain"] = df["domain"].apply(lambda x: x[0])
    df["sub_domain"] = df["domain"].apply(lambda x: x[1])
    for domain, group in df.groupby('main_domain'):
        #print(domain)
        domain_accuracies[domain] = calculate_accuracies(group)
    return domain_accuracies


def caculate_overall_accuracy(df):
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)
    overall_results = {}
    chinese_df = df[df['human_language'] == "chinese"]
    english_df = df[df['human_language'] == "english"]
    chinese_results = caculate_accuracies_by_domains(chinese_df)
    english_results = caculate_accuracies_by_domains(english_df)
    #
    overall_results["chinese"] = chinese_results
    overall_results["english"] = english_results
    #
    overall_results["chinese"]["Average"] = calculate_accuracies(chinese_df) 
    overall_results["english"]["Average"] = calculate_accuracies(english_df)
    return overall_results


def load_cache_data(objs, cache_dir):
    left_objs = []
    cached_objs = []
    for uid, obj in tqdm.tqdm(enumerate(objs)):
        obj["uid"] = uid
        cache_path = os.path.join(cache_dir, f"{uid}.json")
        if os.path.exists(cache_path):
            try:
                obj = utils.read_json(cache_path)
                cached_objs.append(obj)
            except Exception as e:
                left_objs.append(obj)
        else:
            left_objs.append(obj)
    print(f"Successfully loaded {len(cached_objs)} cached objs")
    print(f"Left {len(left_objs)} objs to process")
    return left_objs, cached_objs


async def async_start_llm_judgement(obj, args):
    response = re.sub(r'<think>.*?</think>', '', obj["response"], flags=re.DOTALL)
    obj["final_response"] = response
    if obj["human_language"] == "zh":
        prompt = prompts.Code_Judgment_Zh.format(question = obj["question"], target = obj["answer"], predicted_answer = response)
        messages = [{"role": "system", "content": "你是一个智能助手，请根据给定问题、标准答案和模型预测的答案来评估模型的回答是否正确。"}]
        messages.append({"role": "user", "content": prompt})
    else:
        prompt = prompts.Code_Judgment_En.format(question = obj["question"], target = obj["answer"], predicted_answer = response)
        messages = [{"role": "system", "content": "You are an intelligent assistant. Please evaluate whether the model's answer is correct based on the given question, standard answer, and predicted answer."}]
        messages.append({"role": "user", "content": prompt})
    openai_args = {
        "model": args.judge_model,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "messages": messages,
    }
    obj["judgment"] = await utils.async_chat(base_url = args.base_url, api_key = args.api_key, **openai_args)
    correct = "C"
    try:
        match = re.search(r"(A|B|C)", obj["judgment"])
        correct = match.group(0) if match else "C"
    except:
        correct = "C"
    obj["score"] = correct
    utils.save_json(obj, os.path.join(args.cache_dir, f"{obj['uid']}.json"), logging = False)
    return obj


async def async_start_llm_judgements(objs, args):
    async def limited_task(obj, semaphore):
        async with semaphore:  # This will limit concurrent executions
            return await async_start_llm_judgement(obj, args)
    
    semaphore = asyncio.Semaphore(args.workers)
    tasks = [limited_task(obj, semaphore) for obj in objs]
    # Use either regular gather or tqdm_asyncio for progress bar
    if args.progress:
        objs = await tqdm_asyncio.gather(*tasks, desc="Processing")
    else:
        objs = await asyncio.gather(*tasks)
    return objs

def filter_unknown_domains(objs):
    filtered_objs = []
    unknown_cnt = 0
    cnt = 0
    for obj in objs:
        if obj["domain"][0] not in prompts.COMPUTER_SCIENCE_DOMAINS or obj["domain"][1] not in prompts.COMPUTER_SCIENCE_DOMAINS_REVERSED:
            unknown_cnt += 1
            continue
        if obj["response"] is None:
            cnt += 1
            continue
        filtered_objs.append(obj)
    print(f"Filtered out {unknown_cnt} unknown domain samples")
    print(f"Filtered out {cnt} samples without response")
    return filtered_objs


if __name__ == "__main__":
    args = parse_args()
    os.makedirs(args.cache_dir, exist_ok=True)
    if not os.path.exists(os.path.dirname(args.output_path)):
        os.makedirs(os.path.dirname(args.output_path))
    test_data = utils.read_jsonl_file(args.input_path)
    test_data = filter_unknown_domains(test_data)
    expanded_test_data = []
    if isinstance(test_data[0]["response"], list):
        for obj in test_data:
            for response in obj["response"]:
                new_obj = obj.copy()
                new_obj["response"] = response
                expanded_test_data.append(new_obj)
        test_data = expanded_test_data
    print(f"Loaded {len(test_data)} samples from {args.input_path}")
    if not args.evaluation_only:
        left_objs, cached_objs = load_cache_data(test_data, args.cache_dir)
        left_objs = asyncio.run(async_start_llm_judgements(left_objs, args))
        test_data = left_objs + cached_objs
        test_data.sort(key=lambda x: x["uid"])
        utils.write_jsonl_file(test_data, args.output_path)
    else:
        test_data = utils.read_jsonl_file(args.output_path)

    if not args.judgement_only:
        print(f"Evaluating {len(test_data)} samples...")
        for obj in test_data:
            if obj["domain"][0] in ["Natural Language Processing", "Computer Vision"]:
                obj["domain"][0] = "Artificial Intelligence"
            if obj["domain"][0] == "Robotics":
                obj["domain"][0] = "Emerging Technologies"
        results = caculate_overall_accuracy(test_data)
    utils.save_json(results, f"{args.output_path}.results.json")