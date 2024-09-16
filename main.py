
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

def find_task_by_id(task_id):
    # Create an iterator over the tasks
    # task_iterator = iter(tasks)

    # Use next() to find the task with the specified id
    task = next((task for task in tasks if task['id'] == task_id), None)

    return task

print((find_task_by_id(2)))