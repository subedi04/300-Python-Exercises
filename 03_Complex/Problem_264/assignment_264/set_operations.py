from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def set_operations():
    result = None

    if request.method == 'POST':
        set_a = set(map(int, request.form['set_a'].split(',')))
        set_b = set(map(int, request.form['set_b'].split(',')))

        operation = request.form['operation']
        if operation == 'difference':
            result = set_a - set_b
        elif operation == 'symmetric_difference':
            result = set_a.symmetric_difference(set_b)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
