import requests

response = requests.get('http://127.0.0.1:5000/status')
print(response.json())

response = requests.get('http://127.0.0.1:5000/send',
                        json={"username": "nick", "text": "hello"})
print(response.json())

response = requests.get('http://127.0.0.1:5000/history')
print(response.json())