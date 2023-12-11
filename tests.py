import requests, json


def transfer_data_for_training_request():
	url = 'http://127.0.0.1:8000/transfer_data_for_training/'
	file = {'file': open(r'C:\Users\Нарек\Desktop\DataBase.txt', encoding="utf-8")}
	resp = requests.post(url=url, files=file)
	
	print(resp)


def make_request_in_chatgpt():
	text = 'расскажите о ваших услугам  на ремонт бытовой техники и приведите примеры лидов в этой нише'
	url = 'http://127.0.0.1:8000/make_request_in_chatgpt/?text=' + text
	resp = requests.post(url=url)

	data = resp.json()

	print(data['response'])
	

transfer_data_for_training_request()
# make_request_in_chatgpt()