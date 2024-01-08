class ToDoList:
    def __init__(self):
        # Initialize empty lists for tasks and completed tasks.
        self.tasks = []
        self.completed_tasks = []

    def add_tasks(self, tasks):
        # Add multiple tasks to the To-Do list.
        new_tasks = tasks.split(',')
        self.tasks.extend(new_tasks)
        print(f'Tasks {new_tasks} added.')

    def view_tasks(self):
        # Display all tasks in the To-Do list in list format with counts.
        task_count = len(self.tasks)
        print(f"Total tasks: {task_count}")
        if not self.tasks:
            print("To-Do list is empty.")
        else:
            print("Tasks in the To-Do list:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def complete_task(self, task_index):
        # Complete a task based on its index.
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            self.completed_tasks.insert(0, completed_task)  # Insert at the beginning for newest tasks
            print(f'Task "{completed_task}" completed!')
        else:
            print("Invalid task index. No task completed.")

    def view_completed_tasks(self):
        # Display completed tasks from newest to oldest with counts.
        completed_task_count = len(self.completed_tasks)
        print(f"Total completed tasks: {completed_task_count}")
        if not self.completed_tasks:
            print("No tasks have been completed.")
        else:
            print("Completed tasks (from newest to oldest):")
            for index, task in enumerate(self.completed_tasks, start=1):
                print(f"{index}. {task}")

    def clear_tasks(self):
        # Clear all tasks from the To-Do list.
        self.tasks = []
        self.completed_tasks = []
        print("All tasks cleared.")


def print_menu(todo_list):
    # Print the main menu with task counts.
    total_tasks = len(todo_list.tasks)
    total_completed_tasks = len(todo_list.completed_tasks)
    print("\n==== To-Do List ====")
    print(f"Total tasks: {total_tasks} | Total completed tasks: {total_completed_tasks}")
    print("1. Add Task(s)")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. View Completed Tasks")
    print("5. Clear All Tasks")
    print("0. Exit")


def main():
    # Beginning section to enter name.
    user_name = input("Please enter your name: ")
    print(f"Welcome to your virtual To-Do list, {user_name}!")

    # Create an instance of the ToDoList class.
    todo_list = ToDoList()

    # Run the application in a loop until the user chooses to exit.
    while True:
        # Display the main menu with task counts.
        print_menu(todo_list)

        # Get the user's choice.
        choice = input("Enter your choice (0-5): ")

        # Process the user's choice.
        if choice == "0":
            # Exit the application if the user chooses 0.
            print("Thank you for using your virtual To-Do list.")
            break
        elif choice == "1":
            # Prompt the user to enter multiple tasks and add them to the To-Do list.
            tasks_input = input("Enter task(s) separated by commas: ")
            todo_list.add_tasks(tasks_input)
        elif choice == "2":
            # Display all tasks in the To-Do list.
            todo_list.view_tasks()
        elif choice == "3":
            # Prompt the user to enter a task index and complete the task.
            try:
                task_index = int(input("Enter the task index to complete: "))
                todo_list.complete_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == "4":
            # View completed tasks.
            todo_list.view_completed_tasks()
        elif choice == "5":
            # Clear all tasks from the To-Do list.
            todo_list.clear_tasks()
        else:
            # Display an error message for an invalid choice.
            print("Invalid choice. Enter a number (0-5).")


if __name__ == "__main__":
    main()
