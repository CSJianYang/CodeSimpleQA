## Model Inference
```python
export PATH=./miniconda3/envs/python39/bin/:$PATH
cd ./CodeSimpleQA;
INPUT_PATH="./CodeSimpleQA/data/test_data/code_simpleqa_eval_2k.jsonl"
MODEL_NAME="Qwen2.5-Coder-32B-Instruct"
OUTPUT_PATH="./CodeSimpleQA/data/eval_results/${MODEL_NAME}/code_simpleqa_eval_2k.jsonl"
CACHE_DIR="./CodeSimpleQA/data/eval_results/${MODEL_NAME}/cache/"
BASE_URL=""
API_KEY=""
python infer_models.py --input_path ${INPUT_PATH} --output_path ${OUTPUT_PATH} -base_url ${BASE_URL} -api_key ${API_KEY} -model ${MODEL_NAME} -use_api -workers 32
```
## Model Judgment
```python
MODEL_NAME="Qwen2.5-Coder-32B-Instruct"
echo ${MODEL_NAME}
export PATH=./miniconda3/envs/python39/bin/:$PATH
cd ./CodeSimpleQA;
INPUT_PATH="./CodeSimpleQA/data/eval_results/${MODEL_NAME}/code_simpleqa_eval_2k.jsonl"
OUTPUT_PATH=${INPUT_PATH}.judged.jsonl
CACHE_DIR="./CodeSimpleQA/data/eval_results/${MODEL_NAME}/judge_cache/"
BASE_URL=""
python judge_models.py --input_path ${INPUT_PATH} --output_path ${OUTPUT_PATH} --cache_dir ${CACHE_DIR} -workers 1024 -base_url ${BASE_URL}
```

## Citation
If you find our work helpful, please cite:

```bibtex
@article{yang2025codesimpleqa,
  title={CodeSimpleQA: Scaling Factuality in Code Large Language Models},
  author={Yang, Jian and Zhang, Wei and Li, Yizhi and Guo, Shawn and Wang, Haowen and Liu, Aishan and Zhang, Ge and Wang, Zili and Li, Zhoujun and Liu, Xianglong and others},
  journal={arXiv preprint arXiv:2512.19424},
  year={2025}
}
```
