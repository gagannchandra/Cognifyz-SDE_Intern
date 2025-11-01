# -------------------------------------------
# Program: Simple Task Manager (CRUD App)
# Author: Gagan Chandra (Original Work)
# Level: Intermediate
# Objective: Perform Create, Read, Update, Delete on tasks using Python lists.
# -------------------------------------------

class Task:
    """A simple Task class to hold task details."""
    def __init__(self, task_id, title, status="Pending"):
        self.id = task_id
        self.title = title
        self.status = status

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.status}"


# List to store all tasks
tasks = []


def create_task():
    """Create a new task and add it to the list."""
    title = input("Enter task title: ").strip()
    if not title:
        print("⚠️ Task title cannot be empty.")
        return
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task)
    print("✅ Task created successfully!\n")


def read_tasks():
    """Display all tasks."""
    if not tasks:
        print("📭 No tasks available.\n")
        return
    print("\n📋 Task List:")
    for task in tasks:
        print(task)
    print()


def update_task():
    """Update the title or status of an existing task."""
    if not tasks:
        print("⚠️ No tasks to update.\n")
        return
    read_tasks()
    try:
        task_id = int(input("Enter Task ID to update: "))
        task = next((t for t in tasks if t.id == task_id), None)
        if not task:
            print("❌ Task not found.\n")
            return

        print("1. Update Title")
        print("2. Update Status")
        choice = input("Choose an option: ")

        if choice == "1":
            new_title = input("Enter new title: ").strip()
            if new_title:
                task.title = new_title
                print("✅ Title updated successfully!\n")
        elif choice == "2":
            new_status = input("Enter new status (Pending/Done): ").strip().capitalize()
            if new_status in ["Pending", "Done"]:
                task.status = new_status
                print("✅ Status updated successfully!\n")
            else:
                print("⚠️ Invalid status entered.\n")
        else:
            print("⚠️ Invalid choice.\n")
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.\n")


def delete_task():
    """Delete a task by ID."""
    if not tasks:
        print("⚠️ No tasks to delete.\n")
        return
    read_tasks()
    try:
        task_id = int(input("Enter Task ID to delete: "))
        global tasks
        tasks = [t for t in tasks if t.id != task_id]

        # Reassign IDs after deletion
        for index, t in enumerate(tasks, start=1):
            t.id = index

        print("🗑️ Task deleted successfully!\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


def main():
    """Main loop to interact with the user."""
    while True:
        print("========= 🧮 TASK MANAGER =========")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_task()
        elif choice == "2":
            read_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.\n")


# Run the application
if __name__ == "__main__":
    main()
