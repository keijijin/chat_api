import os

import openai

import env



def Ask_ChatGPT(message):
    openai.api_key = os.environ["OPENAI_API_KEY"]

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(
            "You are a helpful assistant.\n"
            "User: Translate this English text to French: 'Hello, how are you?'"
        ),
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = response.choices[0].text.strip()

    return response

if __name__ == '__main__':
    env.setenv()
    message = "大谷翔平について教えて";
    res = Ask_ChatGPT(message)

    print(res)
