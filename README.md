# ChatGPT Flask API

This is a simple Flask API for interacting with OpenAI's ChatGPT, a state-of-the-art language model. This API allows you to send user messages and receive responses from ChatGPT, and supports setting the temperature and maximum response length.

## Requirements

- Python 3.6+
- Flask
- Flask-CORS
- Requests
- An OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/keijijin/chat_api.git
```

2. Change the directory to the cloned repository:

```bash
cd chat_api
```

3. Install the required packages:

```commandline
pip install -r requirements.txt
```

4. Set up your environment variables:

```commandline
export OPENAI_API_KEY=your_openai_api_key
```

## Usage

1. Run the Flask app:

```commandline
python chat_api.py
```

2. Make a POST request to the /ask endpoint with the following JSON payload:

```json
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What's the weather like today?"}
  ],
  "temperature": 0.5,
  "max_tokens": 50
}
```

3. The API will return a JSON response containing the model's reply:

```json
{
  "response": "The weather today is mostly sunny with a high of 75°F and a low of 60°F. There is a slight chance of rain in the afternoon."
}
```

## API Parameters

- `messages`: An array of message objects with `role` (either "system", "user", or "assistant") and `content` (the message text).
- `temperature`: Controls the randomness of the model's output (optional, default: 0.5). Higher values make the output more random, lower values make it more focused.
- `max_tokens`: Limits the length of the model's response (optional, default: 50). The maximum value is 3000.
