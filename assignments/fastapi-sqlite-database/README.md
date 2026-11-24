# 📘 Assignment: FastAPI with SQLite Database

## 🎯 Objective

Learn to connect a FastAPI application to a SQLite database so task data remains available after the application restarts.

## 📝 Tasks

### 🛠️ Create the Database Connection

#### Descrição

Prepare a SQLite database and create the table used to store tasks.

#### Requisitos

O programa concluído deve:

- Use Python's `sqlite3` module to connect to `tasks.db`.
- Create a `tasks` table if it does not already exist.
- Give each task an integer primary key and fields for `title` and `completed`.
- Close database connections after each operation or use a context manager.

### 🛠️ Read Persistent Tasks

#### Descrição

Replace in-memory task storage with database queries for listing and retrieving tasks.

#### Requisitos

O programa concluído deve:

- Define a Pydantic model for task input data.
- Provide `GET /tasks` to return all database tasks.
- Provide `GET /tasks/{task_id}` to return one task by ID.
- Return `404 Not Found` when the requested task ID does not exist.

### 🛠️ Implement Persistent CRUD

#### Descrição

Complete the API by storing create, update, and delete operations in SQLite.

#### Requisitos

O programa concluído deve:

- Provide `POST /tasks` to insert a task and return it with a database-generated ID.
- Provide `PUT /tasks/{task_id}` to update an existing task.
- Provide `DELETE /tasks/{task_id}` to remove an existing task.
- Return `404 Not Found` for update or delete requests targeting an unknown ID.
- Demonstrate persistence by restarting the server and reading previously created tasks.
