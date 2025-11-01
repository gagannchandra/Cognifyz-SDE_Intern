# -------------------------------------------------
# Program: Persistent Task Manager (CRUD + File I/O)
# Author: Gagan Chandra (Original Work)
# Level: Intermediate
# Objective: Save and load tasks using file operations
# -------------------------------------------------

import os

class Task:
    """A simple class representing a task."""
    def __init__(self, task_id, title, status="Pending"):
        self.id = task_id
        self.title = title
        self.status = status

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.status}"

    def to_file_format(self):
        """Convert task to file-storable format."""
        return f"{self.id}|{self.title}|{self.status}\n"


# Global list to store tasks in memory
tasks = []
FILE_NAME = "tasks.txt"


# ---------------- FILE OPERATIONS ---------------- #

def load_tasks():
    """Load tasks from file into the list."""
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    task_id, title, status = parts
                    tasks.append(Task(int(task_id), title, status))
    except Exception as e:
        print(f"⚠️ Error reading file: {e}")


def save_tasks():
    """Save all tasks from memory to file."""
    try:
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(task.to_file_format())
    except Exception as e:
        print(f"⚠️ Error writing to file: {e}")


# ---------------- CRUD OPERATIONS ---------------- #

def create_task():
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if not title:
        print("⚠️ Task title cannot be empty.\n")
        return
    task_id = len(tasks) + 1
    new_task = Task(task_id, title)
    tasks.append(new_task)
    save_tasks()
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
    """Update an existing task's title or status."""
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

        save_tasks()
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.\n")


def delete_task():
    """Remove a task from the list."""
    if not tasks:
        print("⚠️ No tasks to delete.\n")
        return
    read_tasks()
    try:
        task_id = int(input("Enter Task ID to delete: "))
        global tasks
        tasks = [t for t in tasks if t.id != task_id]

        # Reassign IDs after deletion
        for i, t in enumerate(tasks, start=1):
            t.id = i

        save_tasks()
        print("🗑️ Task deleted successfully!\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")


# ---------------- MAIN APPLICATION ---------------- #

def main():
    """Main menu loop."""
    load_tasks()  # Load saved tasks at startup
    while True:
        print("========= 🧮 PERSISTENT TASK MANAGER =========")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        print("==============================================")

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
            print("👋 Exiting... Your tasks are saved!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
