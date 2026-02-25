from datetime import datetime
from rich.table import Table
from rich.console import Console

console = Console()

def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    table = Table(title="Task Manager")
    table.add_column('Id')
    table.add_column('Description')
    table.add_column('Status')
    table.add_column("Created At")
    table.add_column("Updated At")

    for task in tasks:
        created = datetime.fromisoformat(task["createdAt"]).strftime("%d %b %Y %H:%M")
        updated = datetime.fromisoformat(task["updatedAt"]).strftime("%d %b %Y %H:%M")
        
        table.add_row(task['id'],task['description'],str(task['status']),created,updated)

    console.print(table)
