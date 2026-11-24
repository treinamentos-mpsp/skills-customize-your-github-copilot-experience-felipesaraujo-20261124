# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Learn to build a REST API in Python using the FastAPI framework. You will define endpoints, validate request data, and implement in-memory CRUD operations.

## 📝 Tarefa

### 🛠️ Create a FastAPI Application

#### Descrição

Start the application and create a root endpoint that confirms the API is running.

#### Requisitos

O programa concluído deve:

- Import `FastAPI` and create an application instance.
- Define a `GET /` endpoint that returns a JSON object.
- Include a useful status message in the JSON response.
- Run the application locally with `uvicorn main:app --reload`.

### 🛠️ Add a Task Resource

#### Descrição

Create an in-memory collection of tasks and expose endpoints to list tasks and retrieve one task by ID.

#### Requisitos

O programa concluído deve:

- Define a Pydantic model containing `title` and `completed` fields.
- Store tasks in a Python list or dictionary.
- Define a `GET /tasks` endpoint that returns all tasks.
- Define a `GET /tasks/{task_id}` endpoint that returns the matching task.
- Return an appropriate not-found response when the task ID does not exist.

### 🛠️ Implement CRUD Operations

#### Descrição

Complete the task resource by allowing clients to create, update, and delete tasks.

#### Requisitos

O programa concluído deve:

- Define `POST /tasks` to create a task with a unique numeric ID.
- Define `PUT /tasks/{task_id}` to replace or update an existing task.
- Define `DELETE /tasks/{task_id}` to remove an existing task.
- Return `404 Not Found` for update or delete requests with an unknown ID.
- Test each endpoint using `/docs` or another HTTP client.
