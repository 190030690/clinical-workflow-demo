from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
tasks = []

class TaskInput(BaseModel):
    title: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks")
def create_task(task: TaskInput):
    new_task = {"id": len(tasks) + 1, "title": task.title}
    tasks.append(new_task)
    return new_task

@app.get("/tasks")
def list_tasks():
    return tasks
