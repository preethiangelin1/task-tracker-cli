import argparse
from .service import add_task, list_tasks, update_tasks, delete_tasks, mark_in_progress, mark_done
from .utils import print_tasks

def run():
        
    parser = argparse.ArgumentParser(prog="task-cli")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    list_parser = subparsers.add_parser("list", help="list all tasks")
    list_parser.add_argument("status", nargs="?", help="filter tasks by status")

    update_parser = subparsers.add_parser("update",  help="Update a task")
    update_parser.add_argument("id", help="Id of the task to be updated")
    update_parser.add_argument("description", help="description of the task to be updated")

    delete_parser = subparsers.add_parser("delete",  help="delete a task")
    delete_parser.add_argument("id", help="Id of the task to be deleted")

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress",  help="Mark a task as in progress")
    mark_in_progress_parser.add_argument("id", help="id of the task to be marked as in progress" )

    mark_done_parser = subparsers.add_parser("mark-done",  help="Mark a task as done")
    mark_done_parser.add_argument("id", help="id of the task to be marked as done" )

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)

    elif args.command == "list":
        tasks = list_tasks(args.status)
        print_tasks(tasks)

    elif args.command == "update":
        update_tasks(args.id,args.description)

    elif args.command == "delete":
        delete_tasks(args.id)

    elif args.command == "mark-in-progress":
         mark_in_progress(args.id)

    elif args.command == "mark-done":
         mark_done(args.id)

  

