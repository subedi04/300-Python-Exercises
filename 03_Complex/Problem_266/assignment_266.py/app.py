from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        base = float(request.form['base'])
        height = float(request.form['height'])
        area = 0.5 * base * height
        return render_template('result.html', area=area)
    except ValueError:
        return "Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    app.run()
