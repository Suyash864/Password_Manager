def main():
  add_task = []

  while True:
    print("...To Do List...")
    print("1. Add a task")
    print("2. Show task")
    print("3. Mark task as completed")
    print("4. Exit")

    choice = input("Enter your choice: ")
    try:
      choice = int(choice)
    except ValueError:
      print("Enter valid number")
      continue

    if choice == 1:
      task = input("Enter the task: ")
      add_task.append(task)
      print("Task added successfully!\n\n")

    elif choice == 2:
      if not add_task:
        print("No tasks found.\n")
      else:
        print("Tasks:")
        for i , task in enumerate(add_task, start=1):
          print(f"{i}. {task}")
        print()
      
    elif choice == 3:
      if not add_task:
        print("No tasks to mark as completed")
      else:
        print("Tasks:")
        for i , task in enumerate(add_task, start=1):
          print(f"{i}. {task}")
        task_number = int(input("Enter the task number to mark as completed: "))
        try:
          if 1 <= task_number <= len(add_task):
            add_task[task_number - 1] = add_task[task_number - 1] + " (completed)"
            print("Task marked as completed!\n")
          else:
            print("Invalid task number.\n")
        except ValueError:
          print("Enter valid number.\n")

    else:
      print("Exiting...")
      break

main()