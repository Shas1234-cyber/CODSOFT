# A To-Do List application is a useful project that helps users manage
#  and organize their tasks efficiently. This project aims to create a
#  command-line or GUI-based application using Python, allowing
#  users to create, update, and track their to-do list
import json
import os

TASKS_FILE = "tasks.json"

tasks = []
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as f:
        tasks = json.load(f)

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def show_menu():
    print("\nTO-DO LIST")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task done")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks")
    else:
        print("\nTASKS:")
        for i, task in enumerate(tasks, 1):
            status = "DONE" if task["done"] else "NOT DONE"
            print(f"{i}. {task['name']} ({status})")

def add_task():
    task_name = input("\nTask: ").strip()
    if task_name:
        tasks.append({"name": task_name, "done": False})
        save_tasks()
        print("Task added")
    else:
        print("Empty task")

def mark_done():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nTask number to mark done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num-1]["done"] = True
                save_tasks()
                print("Task marked done")
            else:
                print("Invalid number")
        except ValueError:
            print("Enter number")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nTask number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num-1)
                save_tasks()
                print(f"Deleted: {deleted_task['name']}")
            else:
                print("Invalid number")
        except ValueError:
            print("Enter number")

while True:
    show_menu()
    choice = input("\nChoice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("\nGoodbye")
        break
    else:
        print("Invalid choice")
 
