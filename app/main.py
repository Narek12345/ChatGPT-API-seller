from fastapi import FastAPI
from fastapi import UploadFile

from llama_index import Document, VectorStoreIndex

import os

CHATGPT_TOKEN = os.getenv("CHATGPT_TOKEN")

app = FastAPI()


@app.post('/transfer_data_for_training')
async def transfer_data_for_training(file: UploadFile):
	"""We accept the .txt file, which we then send to ChatGPT for trainig."""
	text = await file.read()
	documents = [Document(text=text)]
	index = VectorStoreIndex.from_documents(documents)
