# consumers.py

import json
from openai import AsyncOpenAI

from channels.generic.websocket import AsyncWebsocketConsumer

client = AsyncOpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)
class Myconsumers(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        print(f"Connection closed with code {close_code}")

    async def receive(self, text_data=None, bytes_data=None):
        # for i in range(10):
        #     await self.send(json.dumps({"message":i}))
        #     time.sleep(1)
        #     print(i)
        input_data = json.loads(text_data)
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": '''Role and Goal: I am Style Scribe, specialized in crafting copy for fashion and luxury products. I create content with a creative hook, detail inspiration, features, and conclude effectively, mimicking the style of provided examples.

Constraints: I focus on unique, engaging content that embodies elegance, avoiding generic descriptions. My style mirrors the sophistication of the luxury and fashion industry.

Guidelines: I integrate detailed product information into the copy, ensuring a cohesive narrative. My responses are comprehensive, reflecting the product's exclusivity and the style of the example provided.

Clarification: I will seek clarification if needed to accurately match the style of the example.

Personalization: My communication style blends formal professionalism with creative flair, adapting to the brand's voice. I meticulously mirror the style of any example provided, ensuring consistency and a tailored experience for the fashion and luxury market.

language: I will use chinese to answer the question.'''},
                {"role": "user",
                 "content": f'''产品信息：{input_data['product']}\n背景：{input_data['background']}\n灵感：{input_data['inspiration']}\n核心元素：{input_data['core']}\n语气风格：{input_data['style']}\n,你需要参考的例子如下（注意撰写的文案不应和例子过度雷同，应该保持原创性）：标题：唤山者系列 | 登顶四姑娘山巅，重现跑者热力
摘要：山就在那里
从古至今，山的力量，山的精神
早已存在我们每个人的内心深处
即使山离你再远
现在，
山的精神
也将被再度唤醒，点燃，和重新演绎
我们以中国三座名山为灵感
推出SALOMON r唤山者」系列
将山的精神，与内心重新连接

内容：
「唤山者」系列首发鞋款XT-6
四姑娘山
我们捕捉攀登四姑娘山的热情
化为热力图，点燃你探索不息的向往

从高山热力图汲取设计灵感
点燃探索不息的向往
捕捉跑者攀登热情，将山与人合二为一

高饱和色系，幻化纷繁色彩
以独特视角，演绎四姑娘山海拔高度
用绚烂色彩，展露对山野精神的无限向往

以高山热力图谱为鞋面着以斑斓之色
与绿、紫、红三色鞋底和谐相应
鞋盒同款印花，捕捉越野跑者炽热之心
独立编号山魂卡，标志无可替代的山地灵魂

越野
踏山而行
为恶劣环境下的长距离比赛而生的XT-6
具备优越的越野性能

舒适缓震ACS中底科技
(AGILE CHASSIS SYSTEM)
确保攀登之时，脚感舒适稳定

搭载Contagrip@高抓地力外底
与TPU薄膜相互配合
耐磨同时保证优越的抓地性能
翻越山川，无惧地形
唤醒山的灵魂，点燃山的活力
汲取三大名山之精神，缔造三双经典跑鞋
SALOMON唤山者 」系列未完待续
'''},
            ],
            stream=True,
        )
        print(f"产品信息：{input_data['product']}/背景：{input_data['background']}/灵感：{input_data['inspiration']}/核心元素：{input_data['core']}/语气风格：{input_data['style']}")
        async for contents in response:
            # if 'content' in contents['choices'][0]['delta']:
            if contents.choices[0].delta.content is not None:
                new = contents.choices[0].delta.content.replace("\n", "<br>")
                await self.send(json.dumps({"message": new}))
        await self.send(json.dumps({"state":1}))


