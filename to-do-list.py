import json

def load_todo_list():
    try:
        with open("todo_list.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todo_list(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)

def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Added: {task}")

def mark_task_as_done(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        task = todo_list[task_index - 1]
        print(f"Marked as done: {task}")
        todo_list.pop(task_index - 1)
    else:
        print("Invalid task index.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(todo_list, task)
            save_todo_list(todo_list)
        elif choice == "3":
            display_todo_list(todo_list)
            task_index = int(input("Enter the task number to mark as done: "))
            mark_task_as_done(todo_list, task_index)
            save_todo_list(todo_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
