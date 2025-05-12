import sys
import json
import os

TODO_FILE = 'todos.json'

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f)

def add_task(task):
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print(f"Added: {task}")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
        return
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")

def delete_task(index):
    todos = load_todos()
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        save_todos(todos)
        print(f"Deleted: {removed}")
    else:
        print("Invalid index.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [add|list|delete] [task]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "delete" and len(sys.argv) > 2:
        try:
            delete_task(int(sys.argv[2]) - 1)
        except ValueError:
            print("Please provide a valid task number.")
    else:
        print("Invalid command.")
