# -*- coding: utf-8 -*-
# @Time : 2024/9/19 20:49
# @Author : dk
# @Contact: dongkz@outlook.com
# @File : qwen25wrapper.py
import requests
import json

# API 端点
url = "http://127.0.0.1:8000/v1/chat/completions"

# 请求的 JSON 数据
data = {
    "model": "qwen-25b",
    "messages": [
        {"role": "user", "content": "你好"}
    ]
}

# 发送 POST 请求
response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

# 输出响应内容
if response.status_code == 200:
    print("Response JSON:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
