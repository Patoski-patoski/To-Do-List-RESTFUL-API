#!/usr/bin/python3
"""app module"""

from flask import Flask, jsonify, request, abort, make_response
from auth import auth
from utils import make_public_task

app = Flask(__name__)


@auth.get_password
def get_password(username: str):
    if username == 'patrick':
        return 'Hello'
    return None


@auth.error_handler
def unauthorized():
    return jsonify({'error': "Unauthorized access"}, 401,)


tasks = [
    {
        'id': 1,
        'title': "Set up your GitHub account",
        'description': "Create a new GitHub account, push your first repository.",
        'done': False
    },
    {
        "id": 2,
        "title": "Complete onboarding documentation",
        "description": "Read through the company's onboarding documentation and complete the required forms.",
        "done": False
    },
    {
        "id": 3,
        "title": "Attend team meeting",
        "description": "Join the weekly team meeting to discuss current projects and updates.",
        "done": False
    }
]


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({"Error": f"{error}"}), 404)


@app.route('/todo/api/v1.0/tasks', strict_slashes=False)
@auth.login_required
def get_tasks():
    return jsonify({"tasks": [make_public_task(task) for task in tasks]})


@app.route('/todo/api/v1.0/tasks/<int:task_id>')
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task':  [make_public_task(t) for t in task]})


@app.route('/todo/api/v1.0/tasks', methods=['POST'], strict_slashes=False)
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    new_id = tasks[-1]['id'] + 1
    task = {
        'id': new_id,
        'title': request.json.get('title'),
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({"new task!": task}), 201


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404, description="Task not found")

    if not request.json:
        abort(400, description="Request body must be JSON")

    title = request.json.get('title')
    description = request.json.get('description')
    done = request.json.get('done')

    # Validate the input
    if title is not None and not isinstance(title, str):
        abort(400, description="Title must be a string")

    if description is not None and not isinstance(description, str):
        abort(400, description="Description must be a string")

    if done is not None and not isinstance(done, bool):
        abort(400, description="Done must be a boolean")

    # Update task with valid fields only
    task.update({
        'title': title or task['title'],
        'description': description or task['description'],
        'done': done if done is not None else task['done']
    })

    return jsonify({'task': task})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404, description="Task not found")
    tasks.remove(task)
    return jsonify({'message': f'Task {task_id} deleted successfully'}), 200


if __name__ == "__main__":
    app.run(debug=True)
