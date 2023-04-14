import os
import json
import requests

# APIキーの設定
import env

env.setenv()
api_key = os.environ["OPENAI_API_KEY"]

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "大谷翔平について教えて"}]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
response_json = response.json()

print(response_json["choices"][0]["message"]["content"].strip())
