import json
import os

FILE_PATH = "data/tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

def delete_task(tasks, index):
    tasks.pop(index)
    save_tasks(tasks)

def mark_done(tasks, index):
    tasks[index]["done"] = True
    save_tasks(tasks)