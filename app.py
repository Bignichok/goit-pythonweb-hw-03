from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)
DATA_FILE = 'storage/data.json'

def save_message(username: str, message: str):
    if not os.path.exists(DATA_FILE):
        data = {}
    else:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    timestamp = datetime.now().isoformat()
    data[timestamp] = {"username": username, "message": message}

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        save_message(username, message)
        if username and message:
            return redirect(url_for('index'))
        return redirect(url_for('index'))
    return render_template('message.html')

@app.route('/read')
def read():
    if not os.path.exists(DATA_FILE):
        messages = {}
    else:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            try:
                messages = json.load(f)
            except json.JSONDecodeError:
                messages = {}

    return render_template('read.html', messages=messages)
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
