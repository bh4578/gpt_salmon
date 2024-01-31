import json

import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

key = "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"

def get_gpt3(**input):

    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "现在你是一个文案专家，需要通过我给定的信息与要求为产品撰写宣传文案，每个信息点以‘/’分隔。"},
            {"role": "user", "content": f"产品信息：{input['product']}/背景：{input['background']}/灵感：{input['inspiration']}/核心元素：{input['core']}/语气风格：{input['style']}"},
        ],
        stream=True
    )

