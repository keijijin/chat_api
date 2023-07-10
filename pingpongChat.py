import json
import logging
import os
import requests
from dotenv import load_dotenv
import argparse

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

def Ask_ChatGPT(messages, temperature=0.5, max_tokens=50):
    max_tokens = min(max_tokens, 3000)

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "n": 3
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    if 'error' in response_json:
        print("エラー: ", response_json['error']['message'])
        return None

    return response_json["choices"][0]["message"]["content"].strip()

def summarize_context(messages):
    summary_request = messages + [{"role": "assistant", "content": "要約してください: {0}".format(messages[-1]['content'])}]
    summary = Ask_ChatGPT(summary_request)
    print("要約：", summary)
    return summary

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--temperature', type=float, help='The temperature for the response generation (default: 0.5)',
                        default=0.5)
    parser.add_argument('--max_tokens', type=int, help='The maximum number of tokens for the response (default: 50)',
                        default=50)
    args = parser.parse_args()

    temperature = args.temperature
    max_tokens = args.max_tokens

    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        message = input("問い：")
        if message.lower() == "exit":
            break

        messages.append({"role": "user", "content": message})

        # If context is too long, try summarizing it
        if sum(len(msg["content"]) for msg in messages) > 4096 - max_tokens:
            summary = summarize_context(messages)
            messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "assistant", "content": summary}]

        res = Ask_ChatGPT(messages, temperature=temperature, max_tokens=max_tokens)

        if res is not None:
            print("答え：", res)
            messages.append({"role": "assistant", "content": res})

        # print(messages)
