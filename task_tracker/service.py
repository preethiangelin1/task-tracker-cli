from datetime import datetime
from .storage import load_tasks, save_tasks
from .models import Task

now = datetime.now().isoformat()


def add_task(description):
    tasks = load_tasks()
    task = Task(description)
    tasks.append(task.to_dict())
    save_tasks(tasks)

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t["status"] == status]
    return tasks

def update_tasks(id,description):
    print(id,description)
    tasks = load_tasks()
    print(tasks)
    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updatedAt"] = now
    save_tasks(tasks)

def delete_tasks(id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
    save_tasks(tasks)

def mark_in_progress(id):
    tasks = load_tasks()
    for task in tasks:
            if task["id"] == id:
                task["status"] = "in-progress"
    save_tasks(tasks)

def mark_done(id):
    tasks = load_tasks()
    for task in tasks:
            if task["id"] == id:
                task["status"] = "done"
    save_tasks(tasks)