import openai
import os
from openai import OpenAI

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.base_url = "https://api.closeai-proxy.xyz/v1"
COMPLETION_MODEL = "text-davinci-003"

prompt = """
Consideration product : 工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具

1. Compose human readable product title used on Amazon in english within 20 words.
2. Write 5 selling points for the products in Amazon.
3. Evaluate a price range for this product in U.S.

Output the result in json format with three properties called title, selling_points and price_range
"""


# def get_response(prompt):
#     completions = openai.completions.create(
#         model=COMPLETION_MODEL,
#         prompt=prompt,
#         max_tokens=512,
#         n=1,
#         stop=None,
#         temperature=0.0,
#     )
#     message = completions.choices[0].text
#     return message

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # base_url="https://api.openai-proxy.org/v1",
    base_url="https://api.closeai-proxy.xyz/v1",
)

completion = client.completions.create(
    prompt=prompt,
    max_tokens=512,
    n=1,
    stop=None,
    temperature=0.0,
    model=COMPLETION_MODEL,
)

message = completion.choices[0].text
print(message)


# print(get_response(prompt))
