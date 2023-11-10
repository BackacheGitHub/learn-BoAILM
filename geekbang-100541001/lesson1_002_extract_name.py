import openai
import os
from openai import OpenAI

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.base_url = "https://api.closeai-proxy.xyz/v1"
COMPLETION_MODEL = "text-davinci-003"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.closeai-proxy.xyz/v1",
)

prompt = """
Man Utd must win trophies, says Ten Hag ahead of League Cup final

请将上面这句话的人名提取出来，并用json的方式展示出来
"""


def get_response(p):
    completions = client.completions.create(
        prompt=p,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.0,
        model=COMPLETION_MODEL,
    )
    message = completions.choices[0].text
    return message


print(get_response(prompt))
