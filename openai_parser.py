import openai
import dotenv
import os

dotenv.load_dotenv()
OPEN_AI_KEY = os.getenv("CHAT_GPT")

openai.api_key = OPEN_AI_KEY


def get_response(message):
    message = str(message)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
        ]
    )
    return response["choices"][0]["message"]["content"]