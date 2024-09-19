# model_start

## 目的

通过封装各类模型的openai风格的api实现一键切换调用各类模型
大致格式如下：

```python
from langchain_openai import ChatOpenAI

endpoint_url = 'http://127.0.0.1:9999/v1/'
llm = ChatOpenAI(api_key="EMPTY",
                 base_url=endpoint_url)

if __name__ == '__main__':
    print(llm.invoke("hello"))
```

## 支持的模型

* chatglm-6b
* chatglm2-6b
* chatglm3-6b
* glm4-9b-chat
* qwen2系列
* qwen2.5系列

## 调用步骤

1. 通过FastAPI启动模型，设置为openai风格的API
2. 通过langchain启动调用api


## 采用的版本

* python==3.8-3.10
* transformers==4.40.0

