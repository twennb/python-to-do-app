"""A simple CLI based to-do list app"""
# Adding file handling to locally save the list
# in a .txt file.
# Adding function to load saved file on program start to
# import the saved list items.

import sys

task_list = []


def add_task(task):
    """function to add tasks to list"""
    task_list.append(task)
    print(f"\nAdding task '{task}'\n")


def remove_task(task):
    """function to remove tasks from list"""
    try:
        task_list.remove(task)
        print(f"\nRemoving task '{task}'\n")
    except ValueError:
        print(f"\nNo task '{task}' found to remove..\n")


def view_tasks():
    """function to view tasks currently in list"""
    print(f"\nCurrent tasks: {task_list}\n")


def exit_program():
    """function to exit the app"""
    ask_save = input("\nDo you want to save before exiting (yes/no): ")

    if ask_save == "yes":
        save_list()
        print("\nExiting the program...\n")
        sys.exit()
    elif ask_save == "no":
        print("\nExiting the program...\n")
        sys.exit()
    else:
        print("\nInvalid input!\n")


def save_list():
    """function for locally saving list between sessions"""
    print("\nSaving list...\n")
    with open("todo-list.txt", "w", encoding="utf-8") as file:
        for task in task_list:
            file.write(task + "\n")


def load_list():
    """function for loading a saved list on program start"""
    try:
        with open("todo-list.txt", "r", encoding="utf-8") as file:
            for line in file:
                task_list.append(line.strip())
    except FileNotFoundError:
        print("\nSave not found\n")


def main():
    """main app function"""

    load_list()

    while True:
        choice = input(
            "Welcome to the To-Do list!\n"
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
                to_add = input("\nWhat task do you want to add: ")
                add_task(to_add)
            case "remove":
                to_remove = input("\nWhat task do you want to remove: ")
                remove_task(to_remove)
            case "view":
                view_tasks()
            case "exit":
                exit_program()
            case "save":
                save_list()
            case _:
                print("\nInvalid command, try again!\n")


if __name__ == "__main__":
    main()
