# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

numbers = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pandas', methods=['POST'])
def pandas_conversion():
    data = request.get_json()
    df = pd.DataFrame(data)
    df.index = [chr(65 + i) for i in range(len(df))]
    return df.to_html(classes="table table-bordered table-hover")

if __name__ == '__main__':
    app.run(debug=True)
