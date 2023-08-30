from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        num = float(request.form['num'])
        percentage = float(request.form['percentage'])
        result = (percentage / 100) * num
        return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
