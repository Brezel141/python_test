# Create an empty list to store tasks
to_do_list = []

# Function to add a task to the list
def add_task():
    task = input("Enter a task: ")  # Prompt the user for a task
    to_do_list.append({"task": task, "completed": False})  # Add the task to the list with a completion status
    print(f"Task '{task}' added to the list.")  # Print a confirmation message

# Function to view the list of tasks
def view_list():
    print("List of tasks:")
    for i, item in enumerate(to_do_list, start=1):
        task_status = "Done" if item["completed"] else "Not Done"
        print(f"{i}. {item['task']} - [{task_status}]")  # Display each task with a completion status

# Function to mark a task as completed
def mark_completed():
    view_list()
    task_num = int(input("Enter the task number to mark as completed: ")) - 1  # Subtract 1 to match the list index
    if 0 <= task_num < len(to_do_list):
        to_do_list[task_num]["completed"] = True
        print(f"Task '{to_do_list[task_num]['task']}' marked as completed.")
    else:
        print("Invalid task number. Please try again.")

# Function to remove a task from the list
def remove_task():
    view_list()
    task_num = int(input("Enter the task number to remove: ")) - 1  # Subtract 1 to match the list index
    if 0 <= task_num < len(to_do_list):
        removed_task = to_do_list.pop(task_num)
        print(f"Task '{removed_task['task']}' removed from the list.")
    else:
        print("Invalid task number. Please try again.")

# Main loop
while True:
    print("\nChoose an operation:")
    print("1. Add a task")
    print("2. View the list of tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")

    choice = input("Enter the operation number: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_list()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Goodbye!")
        break  # Exit the program if '5' is chosen
    else:
        print("Invalid choice. Please try again.")  # Handle invalid choices


