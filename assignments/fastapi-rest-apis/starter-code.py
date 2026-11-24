from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    title: str
    completed: bool = False


# TODO: Add a collection to store tasks in memory.

tasks = {}
next_task_id = 1


@app.get("/")
def read_root():
    # TODO: Return a JSON object that identifies the API.
    pass


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks together with their IDs.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Return the requested task or raise HTTPException with status 404.
    pass


@app.post("/tasks")
def create_task(task: Task):
    # TODO: Create a task, assign it a unique ID, and return it.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    # TODO: Replace the existing task or raise HTTPException with status 404.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the task or raise HTTPException with status 404.
    pass
