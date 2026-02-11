import jsonlines
import pandas as pd
import os
import math
import multiprocessing as mp
import traceback
import tqdm
import itertools
import re
import json
import itertools
import subprocess
import hashlib
import string
import time
from openai import OpenAI, AsyncOpenAI
from openai import AsyncOpenAI


def get_all_choices(completion):
    contents = []
    for i, choice in enumerate(completion.choices):
        content = choice.message.content
        contents.append(content)
    return contents if len(contents) > 1 else contents[0]


async def async_chat(base_url = "", api_key = "", **openai_args):
    async_client = AsyncOpenAI(
        api_key = api_key,  
        base_url = base_url,
        timeout = 1000,
        max_retries = 5,
    )
    try:
        completion = await async_client.chat.completions.create(**openai_args)
        res = get_all_choices(completion)
        if res is not None:
            return res
        return None
    except Exception as e:
        return None


def read_jsonl_file(file_name, max_sentence=None):
    data = []
    with jsonlines.open(file_name, "r") as r:
        for i, obj in tqdm.tqdm(enumerate(r)):
            if max_sentence is not None and i >= max_sentence:
                return data
            data.append(obj)
    return data

def safe_read_jsonl_file(file_name, max_sentence=None):
    data = []
    with open(file_name, "r", encoding="utf-8", errors="ignore") as r:
        for i, line in tqdm.tqdm(enumerate(r)):
            try:
                obj = json.loads(line)
                if max_sentence is not None and i >= max_sentence:
                    return data
                data.append(obj)
            except:
                continue
    return data

def read_json_file(path):
    with open(path, "r") as r:
        objs = json.load(r)
    print(f"Successfully loading from {path}")
    return objs

def write_file(content, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as w:
        w.write(content)
    print(f"Successfully saving to {path}")

def write_jsonl_file(objs, path, chunk_size = 1):
    os.makedirs(os.path.dirname(path), exist_ok = True)
    with jsonlines.open(path, "w", flush=True) as w:
        for i in tqdm.tqdm(range(0, len(objs), chunk_size)):
            w.write_all(objs[i: i + chunk_size])
    print(f"Successfully saving to {path}: {len(objs)}")

def save_json(data, filename, indent = 4, logging = True) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
    if logging:
        print(f"Successfully saving to {filename}")

def read_jsonl_file(file_name, max_sentence=None):
    data = []
    with jsonlines.open(file_name, "r") as r:
        for i, obj in tqdm.tqdm(enumerate(r)):
            if max_sentence is not None and i >= max_sentence:
                return data
            data.append(obj)
    return data

    