import json
import os

class TodoApp:
    def __init__(self):
        # self.tasks = []
        
        # check folder "data" exists or not
        path = os.path.abspath(os.path.dirname(__file__)) + "/"
        if not os.path.exists(path + "data"):
            os.makedirs(path + "data")

        # try to load history task from file
        try:
            with open(path + "data/tasks.json", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []
        except:
            print("Load tasks failed")

    def __del__(self):
        # save history tasks
        path = os.path.abspath(os.path.dirname(__file__)) + "/"
        try:
            with open(path + "data/tasks.json", "w") as f:
                json.dump(self.tasks, f)
        except:
            print("Save tasks failed")


    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added!")

    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index)
            print(f"Task '{task['task']}' removed!")
        except IndexError:
            print("Invalid task index.")

    def mark_completed(self, task_index):
        try:
            self.tasks[task_index]["completed"] = True
            print(f"Task '{self.tasks[task_index]['task']}' marked as completed!")
        except IndexError:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{idx}. {task['task']} - {status}")


def main():
    todo_app = TodoApp()

    while True:
        print("\n----- Simple To-Do List -----")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_app.add_task(task)
        elif choice == '2':
            todo_app.view_tasks()
            try:
                task_index = int(input("Enter task index to remove: "))
                todo_app.remove_task(task_index)
            except ValueError:
                print("Please enter a valid index.")
        elif choice == '3':
            todo_app.view_tasks()
            try:
                task_index = int(input("Enter task index to mark as completed: "))
                todo_app.mark_completed(task_index)
            except ValueError:
                print("Please enter a valid index.")
        elif choice == '4':
            todo_app.view_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
