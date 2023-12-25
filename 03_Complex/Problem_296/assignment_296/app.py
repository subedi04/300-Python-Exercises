from flask import Flask, render_template

app = Flask(__name__)

def generate_numbers():
    return list(range(1, 11))

def calculate_square_and_cube(number):
    return {'number': number, 'square': number**2, 'cube': number**3}

@app.route('/')
def index():
    numbers = generate_numbers()
    results = [calculate_square_and_cube(number) for number in numbers]
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
