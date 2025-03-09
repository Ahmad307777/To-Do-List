
from tkinter import *
from tkinter import messagebox

# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove selected task
def remove_task():
    try:
        selected_task = listbox.curselection()
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to clear all tasks
def clear_tasks():
    listbox.delete(0, END)

# Function to save tasks to file
def save_tasks():
    tasks = listbox.get(0, END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks at startup
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        pass

# Main GUI
root = Tk()
root.title("To-Do List")
root.geometry("400x400")
root.resizable(False, False)

Label(root, text="To-Do List App", font=("Arial", 18)).pack(pady=10)

task_entry = Entry(root, width=40)
task_entry.pack(pady=5)

Button(root, text="Add Task", command=add_task).pack(pady=5)
Button(root, text="Remove Task", command=remove_task).pack(pady=5)
Button(root, text="Clear All Tasks", command=clear_tasks).pack(pady=5)

listbox = Listbox(root, width=50, height=10, selectbackground="yellow")
listbox.pack(pady=10)

# Load tasks on startup
load_tasks()

# Save tasks automatically when closing
root.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(), root.destroy()])

root.mainloop()



