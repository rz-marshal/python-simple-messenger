import requests

print('Enter username:')
username = input()

while True:
    print('Enter text:')
    text = input()

    response = requests.get(
        'http://127.0.0.1:5000/send',
         json={"username": "nick", "text": "hello"}
    )


