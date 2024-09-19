# -*- coding: utf-8 -*-
# @Time : 2024/9/19 18:47
# @Author : dk
# @Contact: dongkz@outlook.com
# @File : qwen25_api.py

import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import uuid

# FastAPI 初始化
app = FastAPI()

# 加载模型和 tokenizer
model_name = r"E:\modelStore\Qwen25-15b-instruct"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 定义请求格式
class ChatRequest(BaseModel):
    model: str
    messages: list

# 定义响应格式
class ChatResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: list

@app.post("/v1/chat/completions", response_model=ChatResponse)
async def create_completion(request: ChatRequest):
    # 验证模型名称
    if request.model != "qwen-25b":
        raise HTTPException(status_code=400, detail="Model not supported")

    # 准备对话模板
    messages = request.messages
    prompt = messages[-1]["content"]  # 假设最后一个消息是用户输入
    system_prompt = {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."}
    chat_messages = [system_prompt] + messages

    # 将消息转化为模型输入
    text = tokenizer.apply_chat_template(chat_messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    # 生成回复
    generated_ids = model.generate(**model_inputs, max_new_tokens=512)
    generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]

    # 解码生成的回复
    response_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    # 返回符合 OpenAI API 格式的响应
    return ChatResponse(
        id=str(uuid.uuid4()),  # 生成唯一 id
        object="chat.completion",
        created=int(time.time()),
        model=request.model,
        choices=[
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response_text
                },
                "finish_reason": "stop"
            }
        ]
    )

# 启动 FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
