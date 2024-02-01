import json
from datetime import datetime

tasks = []

def display_menu():
    print("\n===== Personal Task Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'status': 'Not Started'
    }

    tasks.append(task)
    save_tasks()

def view_tasks():
    print("\n===== Task List =====")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - {task['due_date']} ({task['priority']}) - {task['status']}")

def edit_task():
    view_tasks()
    task_index = int(input("Enter the task number to edit: ")) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index]['status'] = input("Enter new status (Not Started/In Progress/Completed): ")
        save_tasks()
        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: ")) - 1

    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_tasks()
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    global tasks
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the Personal Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
