"""A simple CLI based to-do list app"""
# Features:
#  Add task
#  Remove task
#  View tasks
#  Exit program
#
#  app should be constantly prompting the user for input
#  until they choose to exit the app

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
    print("\nExiting the program...\n")


def main():
    """main app function"""
    while True:
        choice = input(
            "Welcome to the To-Do list!\n"
            "You can type:\n"
            "'add' to add a task\n"
            "'remove' to remove a task\n"
            "'view' to see your tasks\n"
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
            case _:
                print("\nInvalid command, try again!\n")


if __name__ == "__main__":
    main()
