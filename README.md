# Todo List API

A simple, strictly RESTful Todo List API built using Flask. This API allows users to manage a list of tasks with operations such as retrieving tasks, adding new tasks, updating existing tasks, and deleting tasks.

The API is secured using basic HTTP authentication and is designed with modern Flask practices, making it easy to extend and integrate with a proper database.

## Features

- Secure HTTP Basic Authentication
- RESTful API for managing tasks (CRUD operations)
- Easily extendable to use a database like SQLite, PostgreSQL, or MySQL
- Error handling and validation for incoming requests
- Structured and readable codebase

## Table of Contents

- [Todo List API](#todo-list-api)
  - [Features](#features)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Steps](#steps)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
    - [Get ALL Tasks](#get-all-tasks)
    - [Get a Single Task](#get-a-single-task)
    - [Create a New Task](#create-a-new-task)
    - [Update an Existing Task](#update-an-existing-task)
    - [Delete a Task](#delete-a-task)
  - [Authentication](#authentication)
  - [Running Tests](#running-tests)
  - [Future Improvements](#future-improvements)
  - [License](#license)

## Installation

### Requirements

Make sure you have the following installed on your machine:

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/todo-api.git
    cd todo-api
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    flask run
    ```

The app will now be running on `http://127.0.0.1:5000/`.

## Usage

You can interact with the API using tools like `curl`, [Postman](https://www.postman.com/), or your web browser. (i'll recommend getting started with PostMan 🙂)

Example of getting all tasks using `curl`:

```bash
curl -u username:password http://127.0.0.1:5000/todo/api/v1.0/tasks
```

## API Endpoints

### Get ALL Tasks

- Endpoint: `/todo/api/v1.0/tasks`
- Method: `GET`
- Authentication: Required
- Description: Returns a list of all onboarding tasks..
  
```json
{
    "tasks": [
        {
            "id": 1
            "title": "Set up your GitHub account",
            "description": "Create a new GitHub account, push your first repository.",
            "done": false
        }
    ...
    ]
}
```

### Get a Single Task

- Endpoint: `/todo/api/v1.0/tasks/<int:task_id>`
- Method: `GET`
- Authentication: Required
- Description: Retrieve a single onboarding task by its ID.

### Create a New Task

- Endpoint: /todo/api/v1.0/tasks
- Method: `POST`
- Authentication: Required
- Description: Create a new task. The `title` field is mandatory.

**`Request body`**:

```json
{
    "title": "Set up your GitHub account",
    "description": "Create a new GitHub account, push your first repository."
}
```

**`Request`**:

```json
{
     "new task!":{
        "id": 3,
        "title": "Attend team meeting",
        "description": "Join the weekly team meeting to discuss current projects and updates.",
        "done": false
    }
}
```

### Update an Existing Task

- Endpoint: `/todo/api/v1.0/tasks/<int:task_id>`
- Method: `PUT`
- Authentication: Required
- Description: Update an existing task with new values.

**`Request body`**:

```json
{
    "title": "Complete onboarding documentation",
    "done": true,
}
```

### Delete a Task

- Endpoint: `/todo/api/v1.0/tasks/<int:task_id>`
- Method: `DELETE`
- Authentication: Required
- Description: Delete a task by its ID.

**`Response`**

```json
{
    "message": "Task 1 deleted successfully"
}
```

## Authentication

This API uses HTTP Basic Authentication for security. You will need to provide your username and password when making API requests.

Username: `patrick`
Password: `HelloPatrick`
You can provide authentication details using tools like curl:

```bash
    curl -u patrick:HelloPatrick http://127.0.0.1:5000/todo/api/v1.0/tasks
```

## Running Tests

To run the test suite (if you have added tests), execute the following command:

```bash
    python -m unittest discover tests/
```

## Future Improvements

- May Implement token-based authentication (e.g., JWT) for better security.
- May Integrate a database (e.g., SQLite, PostgreSQL) using SQLAlchemy for persistence.
- May Add pagination support to the GET /tasks endpoint.
- May Implement a web frontend using a framework like React or Vue.js.
  
## License

This project is licensed under the MIT License - see the LICENSE file for details.

```markdown

1. **Project Title**: Name of the project.
2. **Description**: Short description of what the project does.
3. **Features**: Key features that stand out in the project.
4. **Installation**: Step-by-step instructions to install and run the project.
5. **Usage**: An example of how to use the API (with curl or Postman).
6. **API Endpoints**: A detailed explanation of all the endpoints, the HTTP methods they use, the request format, and response format.
7. **Authentication**: Information on how to authenticate with the API (HTTP Basic Authentication in this case).
8. **Running Tests**: Instructions for running tests.
9. **Future Improvements**: Areas of improvement
10. **License**: Project License
```
