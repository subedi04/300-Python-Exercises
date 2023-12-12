from flask import Flask, render_template

app = Flask(__name__)

# List of student names
students = [
    "John",
    "Alice",
    "Bob",
    "Sam",
    "Eva",
]

# Filter students whose names do not end with 'aa'
filtered_students = [student for student in students if not student.lower().endswith('aa')]

@app.route('/')
def index():
    return render_template('index.html', students=filtered_students)

if __name__ == '__main__':
    app.run(debug=True)
