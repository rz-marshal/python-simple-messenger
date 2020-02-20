from datetime import datetime, time

from flask import Flask, request

app = Flask(__name__)
messages = [
    {'username': 'jack', 'text': 'hello', 'time': time.time()},
    {'username': 'mary', 'text': 'Hi, Jack', 'time': time.time()}
]


@app.route("/")
def hello():
    return "Ok, World"


@app.route("/status")
def status():
    return {
        'status': True,
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    }


@app.route("/history")
def history():
    """
    request: after= float
    response: {"messages": [{"username": "str", "text": "str", "time": float}, ...]]}
    """
    after = float(request.args['after'])

    filtered_messages = [message for message in messages if after < message['time']]

    return {
        'messages': filtered_messages
    }


@app.route("/send", methods=['POST'])
def send():
    """
    request: {"username": "str", "text": "str"}
    response: {"ok": true}
    """
    data = request.json
    username = data['username']
    text = data['text']

    messages.append({'username': username, 'text': text, 'time': time.time()})

    return {"ok": True}


app.run()
