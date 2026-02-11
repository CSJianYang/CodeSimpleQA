MODEL_NAME="Qwen2.5-Coder-32B-Instruct"
echo ${MODEL_NAME}
export PATH=./miniconda3/envs/python39/bin/:$PATH
cd ./CodeSimpleQA;
INPUT_PATH="./CodeSimpleQA/data/eval_results/${MODEL_NAME}/code_simpleqa_eval_2k.jsonl"
OUTPUT_PATH=${INPUT_PATH}.judged.jsonl
CACHE_DIR="./CodeSimpleQA/data/eval_results/${MODEL_NAME}/judge_cache/"
BASE_URL=""
python judge_models.py --input_path ${INPUT_PATH} --output_path ${OUTPUT_PATH} --cache_dir ${CACHE_DIR} -workers 1024 -base_url ${BASE_URL}
