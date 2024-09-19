# -*- coding: utf-8 -*- 
# @Time : 2024/9/19 20:49 
# @Author : dk
# @Contact: dongkz@outlook.com
# @File : langchain_test.py
from qwen25wrapper import QwenLLM

# 初始化自定义 LLM 类
llm = QwenLLM(api_url="http://127.0.0.1:8000/v1/chat/completions")

# 使用 LLM 调用生成
response = llm.invoke("hello")

# 打印生成的响应
print(response)
