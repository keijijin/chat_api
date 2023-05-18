import logging
import os

openaiApiKeyEnv = "OPENAI_API_KEY"
openaiApiKey = "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"

def setenv():
    if openaiApiKeyEnv in os.environ:
        logging.info(openaiApiKeyEnv, "設定済み")
    else:
        os.environ[openaiApiKeyEnv] = openaiApiKey
