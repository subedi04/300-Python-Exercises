from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check_admission():
    result = None

    if request.method == 'POST':
        age = int(request.form['age'])
        marks = float(request.form['marks'])

        if 20 < age <= 25 and 60 <= marks <= 100:
            result = "Congratulations! You are eligible for admission."
        else:
            result = "Sorry, you are not eligible for admission."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
