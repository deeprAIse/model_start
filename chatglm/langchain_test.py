# -*- coding: utf-8 -*- 
# @Time : 2024/9/19 22:03 
# @Author : dk
# @Contact: dongkz@outlook.com
# @File : langchain_test.py

from langchain_openai import ChatOpenAI

# openai格式api启动方式
endpoint_url_openai = 'http://127.0.0.1:8000/v1/'
llm = ChatOpenAI(api_key="EMPTY",
                 base_url=endpoint_url_openai)

if __name__ == '__main__':
    response = llm.invoke("hello")
    print(response.content)
