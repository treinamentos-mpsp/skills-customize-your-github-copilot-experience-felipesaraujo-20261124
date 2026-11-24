import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE_URL = "tasks.db"

app = FastAPI()


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


def get_connection():
    return sqlite3.connect(DATABASE_URL)


def create_table():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


create_table()


@app.get("/tasks")
def list_tasks():
    # TODO: Query all tasks and return them as dictionaries.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Query one task, then return it or raise HTTPException with status 404.
    pass


@app.post("/tasks")
def create_task(task: TaskCreate):
    # TODO: Insert the task and return it with its database-generated ID.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    # TODO: Update the task or raise HTTPException with status 404.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the task or raise HTTPException with status 404.
    pass
