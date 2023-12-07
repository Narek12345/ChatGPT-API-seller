from fastapi import FastAPI
from fastapi import UploadFile

from llama_index import (
	VectorStoreIndex,
	LLMPredictor,
	ServiceContext,
)
from llama_index.llms import OpenAI
from llama_index.readers.schema import Document
from llama_index import download_loader

import os

CHATGPT_TOKEN = os.getenv("CHATGPT_TOKEN")

app = FastAPI()


@app.post('/transfer_data_for_training')
async def transfer_data_for_training(file: UploadFile):
	"""We accept the .txt file, which we then send to ChatGPT for trainig."""
	data = download_loader(file)
	print(data)
