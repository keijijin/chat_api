import os

import openai

from dotenv import load_dotenv

def Ask_ChatGPT(message):
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(
            "You are a helpful assistant.\n"
            f"User: {message}"
        ),
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = response.choices[0].text.strip()

    return response

if __name__ == '__main__':
    load_dotenv()
    message = "大谷翔平について教えて";
    res = Ask_ChatGPT(message)

    print(res)
