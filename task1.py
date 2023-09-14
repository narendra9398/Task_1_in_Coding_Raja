import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect("todo.db")
c = conn.cursor()

# Create tasks table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              priority TEXT,
              due_date TEXT,
              completed INTEGER)''')

def add_task(name, priority, due_date):
    completed = 0  # 0 represents task not completed
    c.execute("INSERT INTO tasks (name, priority, due_date, completed) VALUES (?, ?, ?, ?)",
              (name, priority, due_date, completed))
    conn.commit()
    print("Task added successfully!")

def remove_task(task_id):
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    print("Task removed successfully!")

def mark_task_completed(task_id):
    c.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    print("Task marked as completed!")

def display_tasks():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for task in tasks:
            task_id, name, priority, due_date, completed = task
            status = "Completed" if completed else "Not Completed"
            print(f"Task ID: {task_id}, Name: {name}, Priority: {priority}, Due Date: {due_date}, Status: {status}")
def display_tasks_in_list_view():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Task List:")
        for task in tasks:
            task_id, name, priority, due_date, completed = task
            status = "Completed" if completed else "Not Completed"
            print(f"Task ID: {task_id}, Name: {name}, Priority: {priority}, Due Date: {due_date}, Status: {status}")
            print("-" * 40)  # Separating lines for each task
def save_tasks_to_file(filename):
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        with open(filename, "w") as file:
            file.write("Task List:\n")
            for task in tasks:
                task_id, name, priority, due_date, completed = task
                status = "Completed" if completed else "Not Completed"
                task_info = f"Task ID: {task_id}, Name: {name}, Priority: {priority}, Due Date: {due_date}, Status: {status}\n"
                file.write(task_info)

# ...

# Save tasks to a file named "tasks.txt"


# Close the database connection
# Add tasks
add_task("Finish project", "high", "2023-09-15")
add_task("Buy groceries", "medium", "2023-09-12")
add_task("Call mom", "low", "2023-09-13")

# Remove task
remove_task(2)

# Mark task as completed
mark_task_completed(1)

# Display tasks
display_tasks()

# Close the database connection
display_tasks_in_list_view()
save_tasks_to_file("tasks.txt")

# Close the database connection
conn.close()
