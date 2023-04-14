import logging
import os

openaiApiKeyEnv = "OPENAI_API_KEY"
openaiApiKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def setenv():
    if openaiApiKeyEnv in os.environ:
        logging.info(openaiApiKeyEnv, "設定済み")
    else:
        os.environ[openaiApiKeyEnv] = openaiApiKey