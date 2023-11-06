'''
Write a Web Application program in Python to delete any record from table.
'''

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock data as an example (replace this with your database)
records = [
    {'id': 1, 'name': 'Record 1'},
    {'id': 2, 'name': 'Record 2'},
    {'id': 3, 'name': 'Record 3'}
]

@app.route('/')
def index():
    return render_template('index.html', records=records)

@app.route('/delete', methods=['POST'])
def delete_record():
    record_id = int(request.form['record_id'])
    global records
    records = [record for record in records if record['id'] != record_id]
    return jsonify({'message': 'Record deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
