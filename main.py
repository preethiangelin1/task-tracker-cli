import os
import argparse
import json
from datetime import datetime

tasks = []
TASK_FILE = "tasks.json"


parser = argparse.ArgumentParser(prog="task-cli")

# Create subcommands
subparsers = parser.add_subparsers(dest="command")

# ADD command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", help="Task description")

# list
list_parser = subparsers.add_parser("list", help="list all tasks")
list_parser.add_argument("status", nargs="?", help="filter tasks by status")

# update command
update_parser = subparsers.add_parser("update",  help="Update a task")
update_parser.add_argument("id", help="Id of the task to be updated")
update_parser.add_argument("description", help="description of the task to be updated")

# delete command
delete_parser = subparsers.add_parser("delete",  help="delete a task")
delete_parser.add_argument("id", help="Id of the task to be deleted")

# mark-in-progress command
mark_in_progress_parser = subparsers.add_parser("mark-in-progress",  help="Mark a task as in progress")
mark_in_progress_parser.add_argument("id", help="id of the task to be marked as in progress" )

# mark-done command
mark_done_parser = subparsers.add_parser("mark-done",  help="Mark a task as done")
mark_done_parser.add_argument("id", help="id of the task to be marked as done" )

args = parser.parse_args()

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE) as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

if args.command == "add":
    # read existing tasks from tasks.json
    tasks = load_tasks()
    
    now = datetime.now().isoformat()
    
    # create task dict
    task = {
        "id" : len(tasks) + 1,
        "description" : args.description,
        "status" : "todo",
        "createdAt" : now,
        "updatedAt" : now
    }

    # append new task to existing tasks
    tasks.append(task)

    # write tasks to tasks.json file
    save_tasks(tasks)

elif args.command == "list":
    tasks = load_tasks()
    
    filter_tasks = []

    if args.status is None:
        filter_tasks = tasks
    else:
        for task in tasks:
            if task["status"] == args.status:
                filter_tasks.append(task)
    

    if not filter_tasks:
        print("No tasks found.")
    else:
        print(f"{'ID':<5} {'Description':<25} {'status':<6} {'Created':<20} {'Updated':<20}")
        print("-" * 80)

        for task in filter_tasks:
            created = datetime.fromisoformat(task["createdAt"]).strftime("%d %b %Y %H:%M")
            updated = datetime.fromisoformat(task["updatedAt"]).strftime("%d %b %Y %H:%M")

            print(f"{task['id']:<5} "
                f"{task['description']:<25} "
                f"{str(task['status']):<6} "
                f"{created:<20} "
                f"{updated:<20}")

    
    
elif args.command == "update":
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(args.id):
            task["description"] = args.description
    
    save_tasks(tasks)

elif args.command == "delete":
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == int(args.id):
            tasks.remove(task)
    
    save_tasks(tasks)

elif args.command == "mark-in-progress":
    tasks = load_tasks()

    for task in tasks:
            if task["id"] == int(args.id):
                task["status"] = "in-progress"

    save_tasks(tasks)

elif args.command == "mark-done":
    tasks = load_tasks()

    for task in tasks:
            if task["id"] == int(args.id):
                task["status"] = "done"

    save_tasks(tasks)


else:
    parser.print_help()



