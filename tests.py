import requests, json

URL = 'http://127.0.0.1:8000'


def transfer_data_for_training_request():
	url = URL + '/transfer_data_for_training/'
	file = {'file': open(r'C:\Users\Нарек\Desktop\DataBase.txt', encoding="utf-8")}
	resp = requests.post(url=url, files=file)

	print(resp)


def make_request_in_chatgpt():
	text = 'кто является моей женной'
	url = URL + '/make_request_in_chatgpt/?text=' + text
	resp = requests.post(url=url)

	data = resp.json()

	print(data['response'])


# transfer_data_for_training_request()
make_request_in_chatgpt()
