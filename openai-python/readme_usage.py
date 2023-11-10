import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    # base_url="https://api.openai-proxy.org/v1",
    base_url="https://api.closeai-proxy.xyz/v1",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

message = chat_completion.choices[0].message
print(message)
