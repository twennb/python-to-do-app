"""A simple CLI based to-do list app"""
# Adding file handling to locally save the list
# in a .txt file.
# Adding function to load saved file on program start to
# import the saved list items.

import sys


class ToDoList:
    """class to handle the task list and related methods"""

    def __init__(self):
        self.tasks = []

    def add_task(self):
        """method to add tasks to list"""
        to_add = input("\nWhat task do you want to add: ")
        self.tasks.append(to_add)
        print(f"Adding task '{to_add}'\n")

    def remove_task(self):
        """method to remove tasks from list"""
        to_remove = input("\nWhat task do you want to remove: ")
        try:
            self.tasks.remove(to_remove)
            print(f"Removing task '{to_remove}'\n")
            return
        except ValueError:
            print(f"Invalid input! No task {to_remove} found to remove..")

    def view_tasks(self):
        """method to view tasks currently in list"""
        if not self.tasks:
            print("\nNo tasks to show!\n")
        else:
            print("\nCurrent tasks: ")
            for index, item in enumerate(self.tasks, start=1):
                print(f"{index}. {item}")

    def save_list(self):
        """method for locally saving list between sessions"""
        print("\nSaving list...\n")
        with open("todo-list.txt", "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_list(self):
        """method for loading a saved list on program start"""
        try:
            with open("todo-list.txt", "r", encoding="utf-8") as file:
                for line in file:
                    self.tasks.append(line.strip())
        except FileNotFoundError:
            print("\nSave not found\n")

    def exit_program(self):
        """method to exit the app"""

        while True:
            ask_save = input("\nDo you want to save before exiting (yes/no): ")

            if ask_save == "yes":
                self.save_list()
                print("\nExiting the program...\n")
                sys.exit()
            elif ask_save == "no":
                print("\nExiting the program...\n")
                sys.exit()
            else:
                print("\nInvalid input!\n")


def main():
    """main app function"""

    task_list = ToDoList()

    task_list.load_list()

    while True:
        choice = input(
            "\nWelcome to the To-Do list!\n"
            "You can type:\n"
            "'add' to add a task\n"
            "'remove' to remove a task\n"
            "'view' to see your tasks\n"
            "'save' to save your list\n"
            "'exit' to close the app\n"
            "What would you like to do: "
        )

        choice = choice.lower()
        match(choice.strip()):
            case "add":
                task_list.add_task()
            case "remove":
                task_list.remove_task()
            case "view":
                task_list.view_tasks()
            case "exit":
                task_list.exit_program()
            case "save":
                task_list.save_list()
            case _:
                print("\nInvalid command, try again!\n")


if __name__ == "__main__":
    main()
