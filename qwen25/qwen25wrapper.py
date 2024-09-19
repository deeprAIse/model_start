# -*- coding: utf-8 -*- 
# @Time : 2024/9/19 20:49 
# @Author : dk
# @Contact: dongkz@outlook.com
# @File : qwen25wrapper.py
import requests
from langchain.llms.base import LLM
from typing import Optional, List


# 自定义 LangChain LLM 类
class QwenLLM(LLM):
    api_url: str

    # 定义输出的内容
    class Config:
        arbitrary_types_allowed = True

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        # 定义要发送给 API 的消息
        messages = [{"role": "user", "content": prompt}]

        # 请求的 JSON 数据
        data = {
            "model": "qwen-25b",
            "messages": messages
        }

        # 发送请求到 FastAPI API
        response = requests.post(self.api_url, json=data)

        # 检查请求是否成功
        if response.status_code != 200:
            raise ValueError(f"Error {response.status_code}: {response.text}")

        # 提取生成的文本
        result = response.json()
        content = result['choices'][0]['message']['content']
        return content

    @property
    def _identifying_params(self) -> dict:
        return {"api_url": self.api_url}

    @property
    def _llm_type(self) -> str:
        return "qwen_llm"
