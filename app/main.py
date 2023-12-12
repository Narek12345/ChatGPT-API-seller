from fastapi import FastAPI
from fastapi import UploadFile, File

from llama_index import (
	Document,
	LLMPredictor,
	PromptHelper,
	StorageContext,
	GPTVectorStoreIndex,
	load_index_from_storage,
)

from langchain.llms import OpenAI

from typing import Annotated

import os

os.environ['OPENAI_API_KEY'] = "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"

app = FastAPI()


@app.post('/transfer_data_for_training')
def transfer_data_for_training(file: UploadFile = File(...)):
	"""We accept the .txt file, which we then send to ChatGPT for trainig."""

	try:
		contents = file.file.read()
		with open(file.filename, 'wb') as f:
			f.write(contents)
	except Exception:
		return {"message": "There was an error uploading the file"}
	finally:
		file.file.close()
		os.remove(file.filename)

	text = contents.decode()

	llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name='text-davinci-003', max_tokens=300))
	prompt_helper = PromptHelper(4096, 300, 0.2, chunk_size_limit=600)

	documents = [Document(text=text)]

	index = GPTVectorStoreIndex.from_documents(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

	index.storage_context.persist()

	return "200 OK"


@app.post('/make_request_in_chatgpt')
def make_request_in_chatgpt(text: str):
	"""We make a request to the trained ChatGPT."""
	storage_context = StorageContext.from_defaults(persist_dir='./storage')
	index = load_index_from_storage(storage_context)

	query_engine = index.as_query_engine()
	response = query_engine.query(text)

	return response