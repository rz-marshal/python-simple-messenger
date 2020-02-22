import time
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)
messages = [
    {'username': 'jack', 'text': 'hello', 'time': time.time()},
    {'username': 'mary', 'text': 'Hi, Jack', 'time': time.time()}
]
users = {
    'jack': 'black',
    'mary': '12345'
}


@app.route("/")
def hello():
    return "Ok, World"


@app.route("/status")
def status():
    return {
        'status': True,
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        'messages_count': len(messages),
        'users_count': len(users)
    }


@app.route("/history")
def history():
    """
    request: after= float
    response: {"messages": [{"username": "str", "text": "str", "time": float}, ...]]}
    """
    after = float(request.args['after'])

    filtered_messages = [message for message in messages if after < message['time']]

    return {'messages': filtered_messages}

authorization = 1
@app.route("/send", methods=['POST'])
def send():
    """
    request: {"username": "str", "password": "str", "text": "str"}
    response: {"ok": true}
    """
    data = request.json
    username = data['username']
    password = data['password']
    text = data['text']

    if username in users:
        real_password = users[username]
        if real_password != password:
            return {"ok": False}
    else:
        users[username] = password

    new_message = {'username': username, 'text': text, 'time': time.time()}
    messages.append(new_message)

    return {"ok": True}


app.run()
