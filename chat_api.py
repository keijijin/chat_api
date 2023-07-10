import json
import logging
import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask_chat_gpt():
    input_data = request.get_json()
    messages = input_data.get("messages")
    temperature = input_data.get("temperature", 0.5)
    max_tokens = input_data.get("max_tokens", 50)

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
        return jsonify({"error": response_json['error']['message']})

    return jsonify({"response": response_json["choices"][0]["message"]["content"].strip()})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
