from tkinter import *

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)

root = Tk()
root.title("To-Do List")

entry = Entry(root, width=30)
entry.pack()

Button(root, text="Add Task", command=add_task).pack()
listbox = Listbox(root)
listbox.pack()

root.mainloop()
