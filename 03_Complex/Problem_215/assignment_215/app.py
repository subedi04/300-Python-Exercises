from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            integer_input = int(request.form['integer_input'])
            complex_number = complex(integer_input, 0)
            return render_template('result.html', complex_number=complex_number)
        except ValueError:
            error_message = "Please enter a valid integer."
            return render_template('index.html', error_message=error_message)
    return render_template('index.html', error_message=None)

if __name__ == '__main__':
    app.run(debug=True)
