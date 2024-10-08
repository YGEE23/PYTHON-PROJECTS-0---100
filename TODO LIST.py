'''
A TO-DO LIST PROGRAM
Key Features:
Add a Task: Add tasks with a description, due date, and priority (e.g., high, medium, low).
View Tasks: Show all tasks, but include options to:
Show only incomplete tasks.
Show tasks sorted by due date or priority.
Mark a Task as Complete: Let the user mark a task as completed.
Delete a Task: Allow the user to delete tasks.
Save/Load Tasks: (Optional) Save the task list to a file so the user can close the program and load the tasks back when they reopen it.

'''
# Initialize the list if tasks
tasks = []

#add a new task
def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date DD/MM/YYYY: ")
    priority = input("Enter priority (high/medium/low): ").strip().lower()

    task = {
        "Description": description,
        "Due_Date": due_date,
        "Priority Level": priority,
        "Completed": False
    }
    tasks.append(task)
    print(f"Task: '{description}' added! ")

#view tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, 1): # Numbers each tasks
        status = "Completed" if task ["Completed"] else "Incomplete"
        print(f"{i}. {task['Description']} | Due: {task['Due_Date']} | Priority: {task['Priority Level']} | Status: {status} ")

# Function to mark task as complete
def mark_task_complete():
    view_tasks()
    task_num = int(input("Enter the number of the task to mark as complete: ")) - 1

    if 0 <= task_num < len(tasks): #checks if user input is or is not in the list range
        tasks[task_num]["Completed"] = True
        print(f"Task '{tasks[task_num]['Description']}' marked as complete.")

    else:
        print("Invalid task number.")

# Mark a task as incomplete
def mark_task_incomplete():
    view_tasks()
    task_num = int(input("Enter the number of the task to mark as incomplete: ")) -1

    if 0 <= task_num < len(tasks): # Checks if user input is withing list range.
        tasks[task_num]["Completed"] = False
        print(f"Task '{tasks[task_num]['Description']}' marked Incomplete.")

    else: 
        print("Invaid task number.")


#delete a task
def del_task():

    view_tasks()
    task_num = int(input("Enter index number of the task you want to delete: "))

    if 0 <= task_num < len(tasks):
        deleted_task = tasks.pop(task_num)
        print(f"Task '{deleted_task['Description']}' has been deleted!")

    else:
        print("Invalid task number.")


# Menu selection function

def task_manager():
    while True:
        print("\nTo-Do List Manager")
        print("[1] Add a task")
        print("[2] View a task")
        print("[3] Mark a task as completed")
        print("[4] Mark a taskk as Incomplete")
        print("[5] Delete a task")
        print("[6] Quit")

        choice = input("Select your option: ")

        if choice =='1':
            add_task()

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            mark_task_complete()
        
        elif choice == '4':
            mark_task_incomplete()

        elif choice == '5':
            del_task()
            
        elif choice == '6':
            print("Good bye!")
            break

        else:
            print("Invalid selection, please tru again.")

# Start the task manager func
if __name__ == '__main__':
    task_manager()
