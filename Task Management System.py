tasks = []

while True:
    print("\n--- Task Management Menu ---")
    print("1. Add a new task")
    print("2. Update task status")
    print("3. Delete completed tasks")
    print("4. View all tasks")
    print("5. Filter tasks by priority")
    print("6. Filter tasks by deadline")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        task_description = input("Enter the task description: ")
        deadline = input("Enter the task deadline (YYYY-MM-DD): ")
        priority = input("Enter the task priority (High, Medium, Low): ")
        task = [task_description, deadline, priority, "Not Completed"]
        tasks.append(task)
        print("New task added: ", task)

    elif choice == "2":
        task_description = input("Enter the task description to update: ")
        task_found = False
        for task in tasks:
            if task[0].lower() == task_description.lower():
                task_found = True
                print("Current Task Status: ", task[3])
                new_status = input(
                    "Enter the new status (Completed, In-Progress): "
                )
                task[3] = new_status
                print("Task status updated: ", task)
                break
        if not task_found:
            print("Task not found.")

    elif choice == "3":
        task_description = input("Enter the task description to delete: ")
        task_found = False
        for task in tasks:
            if (
                task[0].lower() == task_description.lower()
                and task[3] == "Completed"
            ):
                tasks.remove(task)
                print("Task ", task_description, " deleted.")
                task_found = True
                break
        if not task_found:
            print("Task not found or not completed.")

    elif choice == "4":
        if tasks:
            print("\n--- Task List ---")
            for task in tasks:
                print(
                    "Task: ",
                    task[0],
                    "Deadline: ",
                    task[1],
                    "Priority: ",
                    task[2],
                    "Status: ",
                    task[3],
                )
        else:
            print("Task list is empty.")

    elif choice == "5":
        priority = input("Enter the priority to filter by: ").capitalize()
        filtered_tasks = []
        for task in tasks:
            if task[2] == priority:
                filtered_tasks.append(task)
        if filtered_tasks:
            print("\n--- Tasks with ", priority, " Priority ---")
            for task in filtered_tasks:
                print(
                    "Task: ",
                    task[0],
                    "Deadline: ",
                    task[1],
                    "Status: ",
                    task[3],
                )
        else:
            print("No tasks found with ", priority, " priority.")

    elif choice == "6":
        deadline = input("Enter the deadline to filter by (YYYY-MM-DD): ")
        filtered_tasks = []
        for task in tasks:
            if task[1] == deadline:
                filtered_tasks.append(task)
        if filtered_tasks:
            print("\n--- Tasks with ", deadline, " Deadline ---")
            for task in filtered_tasks:
                print(
                    "Task: ",
                    task[0],
                    "Priority: ",
                    task[2],
                    "Status: ",
                    task[3],
                )
        else:
            print("No tasks found with ", deadline, " deadline.")

    elif choice == "7":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please try again.")