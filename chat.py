import json
import logging
import os
import openai
import requests
import env
import argparse

env.setenv()
api_key = os.environ["OPENAI_API_KEY"]

def Ask_ChatGPT(message, temperature=0.5, max_tokens=50):
    # print("temp: {}".format(temperature))
    # print("token: {}".format(max_tokens))
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": message}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    return response_json["choices"][0]["message"]["content"].strip()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--temperature', type=float, help='The temperature for the response generation (default: 0.5)', default=0.5)
    parser.add_argument('--max_tokens', type=int, help='The maximum number of tokens for the response (default: 50)', default=50)
    args = parser.parse_args()

    temperature = args.temperature
    max_tokens = args.max_tokens

    while True:
        message = input("問い：")
        if message.lower() == "exit":
            break
        res = Ask_ChatGPT(message, temperature=temperature, max_tokens=max_tokens)
        print("答え：", res)

