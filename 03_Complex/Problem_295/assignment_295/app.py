from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_grade(marks):
    if marks >= 95:
        return 'A+ Grade'
    elif marks >= 80:
        return 'A Grade'
    elif marks >= 70:
        return 'B Grade'
    elif marks >= 60:
        return 'C Grade'
    else:
        return 'Fail'

@app.route('/', methods=['GET', 'POST'])
def index():
    grade = None

    if request.method == 'POST':
        try:
            marks = float(request.form['marks'])
            grade = calculate_grade(marks)
        except ValueError:
            grade = 'Invalid input. Please enter a valid number.'

    return render_template('index.html', grade=grade)

if __name__ == '__main__':
    app.run(debug=True)
