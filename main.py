import json
import os

FILE_NAME = "tasks.json"
def add_task(tasks_list):
    task = input("Enter the task: ")
    new_task = {
        "title": task,
        "completed": False
    }
    tasks_list.append(new_task)
    save_tasks(tasks_list)
    print("✅ Task added!")

def delete_task(tasks_list):
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks_list):
            deleted = tasks_list.pop(task_num - 1)
            save_tasks(tasks_list)
            print(f"🗑️ Deleted: {deleted}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def toggle_task_completion(tasks_list):
    try:
        task_num = int(input("Enter task number to toggle its completion: "))
        if 1 <= task_num <= len(tasks_list):
            tasks_list[task_num - 1]["completed"] = not tasks_list[task_num - 1]["completed"]
            save_tasks(tasks_list)
            print(f"Toggled the completion of task: {tasks_list[task_num - 1]['title']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def view_tasks(tasks_list):
    print("📋 Your tasks:")
    for i, task in enumerate(tasks_list, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['title']}")

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

print("👋 Welcome to the To-Do List App!")

while True:
    print("--------------------------")
    print("\nChoose an option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Toggle task completion")
    print("5. Exit")
    print("--------------------------")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        if not tasks:
            print("📭 No tasks yet.")
        else:
            view_tasks(tasks)

    elif choice == "3":
        if not tasks:
            print("❌ No tasks to delete.")
        else:
            view_tasks(tasks)
            delete_task(tasks)

    elif choice == "4":
        if not tasks:
            print("❌ No tasks to toggle its completion.")
        else:
            view_tasks(tasks)
            toggle_task_completion(tasks)

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❗ Invalid choice. Please try again.")