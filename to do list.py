class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

    def update_task(self, index, new_task):
        if index >= 1 and index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if index >= 1 and index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()

    while True:
        print("\n*** To-Do List Application ***")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '4':
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

