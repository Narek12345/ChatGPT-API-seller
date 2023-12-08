from fastapi import FastAPI
from fastapi import UploadFile

from pydantic import BaseModel

from llama_index import (
	Document,
	VectorStoreIndex,
	LLMPredictor,
	PromptHelper,
	GPTVectorStoreIndex,
)

import os

CHATGPT_TOKEN = os.getenv("CHATGPT_TOKEN")

app = FastAPI()


@app.post('/transfer_data_for_training')
def transfer_data_for_training(file: UploadFile):
	"""We accept the .txt file, which we then send to ChatGPT for trainig."""
	text = file.file.read().decode('windows-1251')
	optimized_text = text.encode('utf-8').decode()

	documents = Document(text=optimized_text)
	# index = GPTVectorStoreIndex.from_documents(documents)

	# Save index.json file in the root folder.
	# index.save_to_disk('index.json')

	# return index
	return documents


@app.post('/make_request_in_chatgpt')
def make_request_in_chatgpt(text: str):
	"""We make a request to the trained ChatGPT."""
	# index = GPTVectorStoreIndex.load_from_disk('index.json')

	# Making a request in ChatGPT.
	# response = index.query(text, response_mode='conpact')

	# return response
	return text