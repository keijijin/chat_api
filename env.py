import logging
import os

openaiApiKeyEnv = "OPENAI_API_KEY"
openaiApiKey = "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"

def setenv():
    if openaiApiKeyEnv in os.environ:
        logging.info(openaiApiKeyEnv, "設定済み")
    else:
        os.environ[openaiApiKeyEnv] = openaiApiKey