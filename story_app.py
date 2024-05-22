from autogen import ConversableAgent

local_phi3_config={
    "config_list": [
        {
            "model": "NotRequired", # Loaded with LiteLLM command
            "api_key": "NotRequired", # Not needed
            "base_url": "http://0.0.0.0:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None # Turns off caching, useful for testing different models
}
local_llama3_config={
    "config_list": [
        {
            "model": "NotRequired", # Loaded with LiteLLM command
            "api_key": "NotRequired", # Not needed
            "base_url": "http://0.0.0.0:4001"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None # Turns off caching, useful for testing different models
}

jack = ConversableAgent(
    "Jack (Phi-3)",
    llm_config=local_phi3_config,
    system_message="你的名字叫Jack，你是一个中文AI作家。你的角色是根据指定主题创作引人入胜且信息丰富的文章，并且根据你的同事Emma的建议来修改和完善你创作的文章，每当你收到Emma的建议时，都要根据Emma的建议给出修改和完善后的完整文章。",
)

emma = ConversableAgent(
    "Emma (llama3)",
    llm_config=local_llama3_config,
    system_message="你的名字叫Emma，你的角色是一个中文AI文章评审员。你的任务是针对你的同事Jack所写的文章评估并提出改进建议，每次对话你都要对文章作出评估并给出修改建议。",
)

chat_result = emma.initiate_chat(jack, message="Jack，请用中文写一篇关于科学家穿遇到未来的文章。", max_turns=3)
