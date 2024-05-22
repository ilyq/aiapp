vllm
https://github.com/vllm-project/vllm


ollama安装  
https://github.com/ollama/ollama/blob/main/docs/linux.md

ollama 模型  
https://github.com/ollama/ollama  
https://ollama.com/library

ollama api 使用
https://github.com/ollama/ollama/blob/main/docs/api.md
https://github.com/ollama/ollama/blob/main/docs/openai.md


ollama 量化说明
https://github.com/ollama/ollama/blob/main/docs/import.md#quantization-reference
```
# 从低到高，理论越高越好
q2_K
q3_K
q3_K_S
q3_K_M
q3_K_L
q4_0 (recommended)
q4_1
q4_K
q4_K_S
q4_K_M
q5_0
q5_1
q5_K
q5_K_S
q5_K_M
q6_K
q8_0
f16
```


ollama 安装 phi3
ollama pull phi3:3.8b

ollama 安装 llama3
ollama pull llama3:8b


litellm ollama 使用  
https://github.com/BerriAI/litellm
https://docs.litellm.ai/docs/providers/ollama#ollama-models


litellm --model ollama/llama3:8b --port 4001
litellm --model ollama/phi3:3.8b


llama2.c 这里有故事数据集
https://github.com/karpathy/llama2.c
https://huggingface.co/datasets/roneneldan/TinyStories



autogen 故事对话
https://www.bilibili.com/video/BV1Pb421b7YC/
https://blog.stoeng.site/20240512.html


autogen litellm 使用ollama示例  
https://microsoft.github.io/autogen/docs/topics/non-openai-models/local-litellm-ollama


unsloth 微调
https://github.com/unslothai/unsloth


samantha-mistral 模型
https://ollama.com/library/samantha-mistral
在哲学、心理学和人际关系方面受过训练的同伴助理。基于Mistral。
