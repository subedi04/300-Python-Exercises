from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    start_time = int(request.form['start_time'])
    end_time = int(request.form['end_time'])
    remaining_time = end_time - int(time.time())
    return jsonify({'remaining_time': remaining_time})

if __name__ == '__main__':
    app.run(debug=True)
