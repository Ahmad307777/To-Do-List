
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = listbox.get(0, END)
        for task in tasks:
            file.write(task + "\n")


