from tkinter import *

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(END, task)
        task_entry.delete(0, END)

root = Tk()
root.title("To-Do List")

task_entry = Entry(root, width=30)
task_entry.pack()

Button(root, text="Add Task", command=add_task).pack()
listbox = Listbox(root)
listbox.pack()

root.mainloop()



