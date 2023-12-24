# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def message_list():
    # Dummy data for demonstration
    messages = [
        {'title': 'Message 1', 'content': 'This is the content of message 1.'},
        {'title': 'Message 2', 'content': 'This is the content of message 2.'},
        # Add more messages as needed
    ]
    return render_template('message_list.html', messages=messages)

@app.route('/message/<int:message_id>')
def message_detail(message_id):
    # Dummy data for demonstration
    message = {'title': f'Message {message_id}', 'content': f'This is the content of message {message_id}.'}
    return render_template('message_detail.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
