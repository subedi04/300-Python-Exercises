from flask import Flask, render_template, request

app = Flask(__name__)

def convert_to_uppercase(input_str):
    if input_str.isupper():
        return input_str, "String is already in uppercase"
    else:
        return input_str.upper(), None

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    message = None

    if request.method == 'POST':
        input_str = request.form['input_str']
        result, message = convert_to_uppercase(input_str)

    return render_template('index.html', result=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
