from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(title="Task Tracker API")

# Mock database
tasks_db = []

# Data model for a Task
class Task(BaseModel):
    id: str
    title: str
    status: str = "pending"

class TaskCreate(BaseModel):
    title: str

@app.get("/health")
def health_check():
    """Used by Kubernetes Liveness/Readiness probes."""
    return {"status": "healthy"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(id=str(uuid.uuid4()), title=task.title)
    tasks_db.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, status: str):
    for task in tasks_db:
        if task.id == task_id:
            task.status = status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            del tasks_db[i]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")