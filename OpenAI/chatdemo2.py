from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def get_chat_completion(messages):
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
    )

prompt = "Briefly explain the Python programming language."
messages = [{"role": "user", "content": prompt}]

chat_completion = get_chat_completion(messages)
gpt_response = chat_completion.choices[0].message.content

print(gpt_response)