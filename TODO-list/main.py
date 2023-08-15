class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in this TODO-list")
        else:
            print(self.tasks)
            for i, j in enumerate (self.tasks, 1):
                print(f'Task {i}: Description: {j.description}, Due Date: {j.due_date}')


    def finished_task(self, task_index):
        try:
            del self.tasks[task_index -1]
        except Exception as e:
            print(f"No such task\n Exception: {e}" )


def main():
    todo_list = ToDoList()

    while True:
        print("\n===== Todo List Application =====")
        print("Press 1 to add task")
        print("Press 2 to view all tasks")
        print("Press 3 to remove task")
        print("Press 4 to exit")

        choice = input ("Enter yor choice (1-4):\n")

        if choice == "1":
            description = input("Write a description for the task: ")
            due_date = input("Write a due_date for the task: ")
            task = Task(description, due_date)
            todo_list.add_task(task)
            print("Task successfully added!")

        elif choice == "2":
            print("\n----- Tasks -----")
            todo_list.view_tasks

        elif choice == "3":
            if not todo_list.tasks:
                print("No tasks in this todo-list")
            else:
                index = int(input("Which task-index do you want to remove? "))
                todo_list.finished_task(index)
                print("Task successfully removed!")

        elif choice == "4":
            break
        
        else:
            print("Unvalid input - press a number between 1 and 4:\n")


if __name__ == "__main__":
    main()
