todo = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour tasks:")
        for t in todo:
            print("-", t)

    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in todo:
            todo.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")