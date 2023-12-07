from fastapi import FastAPI
from fastapi import UploadFile

from llama_index import SimpleDirectoryReader, GPTListIndex, readers, LLMPredictor, PromptHelper
from langchain import OpenAI

import os

CHATGPT_TOKEN = os.getenv("CHATGPT_TOKEN")

app = FastAPI()


@app.post('/transfer_data_for_training')
async def transfer_data_for_training(file: UploadFile):
	"""We accept the .txt file, which we then send to ChatGPT for trainig."""

	max_input_size = 4096
	num_outputs = 300
	max_chunk_overlap = 20
	chunk_size_limit = 600

	# Define LLM.
	llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))
	prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

	documents = SimpleDirectoryReader(file).load_data()

	index = GPTSimpleVectorIndex(
		documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
	)

	index.save_to_disk('index.json')

	return index


