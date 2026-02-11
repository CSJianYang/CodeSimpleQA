
export PATH=./miniconda3/envs/python39/bin/:$PATH
cd ./CodeSimpleQA;
INPUT_PATH="./CodeSimpleQA/data/test_data/code_simpleqa_eval_2k.jsonl"
MODEL_NAME="Qwen2.5-Coder-32B-Instruct"
OUTPUT_PATH="./CodeSimpleQA/data/eval_results/${MODEL_NAME}/code_simpleqa_eval_2k.jsonl"
CACHE_DIR="./CodeSimpleQA/data/eval_results/${MODEL_NAME}/cache/"
BASE_URL=""
API_KEY=""
python infer_models.py --input_path ${INPUT_PATH} --output_path ${OUTPUT_PATH} -base_url ${BASE_URL} -api_key ${API_KEY} -model ${MODEL_NAME} -use_api -workers 32

