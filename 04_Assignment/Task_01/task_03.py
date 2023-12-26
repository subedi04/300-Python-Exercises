'''
Develop a RESTful API that allows users to create, read, 
update, and delete resources using Python and Flask.
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (tasks list)
tasks = [
    {"id": 1, "title": "Task 1", "description": "Description 1", "done": False},
    {"id": 2, "title": "Task 2", "description": "Description 2", "done": False},
]

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Route to get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({'task': task})
    else:
        return jsonify({'error': 'Task not found'}), 404

# Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Route to update a task by ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.get_json()
        task['title'] = data['title']
        task['description'] = data['description']
        task['done'] = data['done']
        return jsonify({'task': task})
    else:
        return jsonify({'error': 'Task not found'}), 404

# Route to delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)

'''
Get all taks
http GET http://127.0.0.1:5000/tasks    


Get a specific task by ID:
http GET http://127.0.0.1:5000/tasks/1


Create a new task:
http POST http://127.0.0.1:5000/tasks title="New Task" description="New Description" done=false


Update a task by ID:
http PUT http://127.0.0.1:5000/tasks/1 title="Updated Task" description="Updated Description" done=true


Delete a task by ID:
http DELETE http://127.0.0.1:5000/tasks/1

'''
