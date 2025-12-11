print("Welcome to CLI To-Do List!")
# Creating a Empty List to store Tasks.
tasks = []
completed_tasks = []
while True:
    print("\n1. Add a Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Mark Task Completed")
    print("5. Clear Completed Tasks")
    print("6. Exit Program")

    choice = int(input("\nEnter Your Choice (1-6): "))
    # Adding New Tasks
    if choice == 1:
        index = 0
        add_task = input("Enter Your Task: ")
        tasks.append(add_task)
    # Viewing All Tasks.
    elif choice == 2:
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")
    elif choice == 3:
    # Deleting a Task
        if len(tasks) == 0:
            print("The List is Empty.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index+1}. {task}")
            del_task = int(input("Enter Your Choice: "))
            tasks.pop(del_task-1)
    # Marking Task as completed
    elif choice == 4:
        if len(tasks) == 0:
            print("The List is Empty.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index+1}. {task}")
            del_task = int(input("Enter Completed Task #: "))
            comp_task = tasks[del_task-1]
            tasks.pop(del_task-1)
            completed_tasks.append(comp_task)
            for task in completed_tasks:
                print(f"Completed Tasks are: \n{task}")
    # Deleting the completed task
    elif choice == 5:
        del completed_tasks[:]
        print("Deleted all completed tasks...")
    elif choice == 6:
        print("The Program is Exiting...")
        break
    else:
        print("Invalid Input!")