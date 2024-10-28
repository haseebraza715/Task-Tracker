import json 
import os
import sys
from datetime import datetime


task_file = 'tasks.json'    

def load_tasks():
    if not os.path.exists(task_file):
        with open(task_file, 'w') as file:
            json.dump([], file)
    with open(task_file, 'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(task_file, 'w') as f:
        json.dump(tasks, f, indent=4)



def add_task(task):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "task": task,
        "status": "todo",
        "created_at": datetime.now().isoformat(),
        "upadted_at": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(task_id,description):
    tasks = load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        print(f"Task with ID {task_id} not found")
        return
    
    task['description'] = description
    task['updated_at'] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task updated successfully")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task deleted successfully")

def mark_task(task_id, status):
    tasks= load_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['status'] = status
        task['updated_at'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task marked as {status}")
    else:
        print(f"Task with ID {task_id} not found")    

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    for task in tasks:
        print(f"{task['id']}: {task['task']} ({task['status']})")


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "update":
        task_id = int(sys.argv[2])
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)
    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == "mark-in-progress":
        task_id = int(sys.argv[2])
        mark_task(task_id, "in-progress")
    elif command == "mark-done":
        task_id = int(sys.argv[2])
        mark_task(task_id, "done")
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()

    