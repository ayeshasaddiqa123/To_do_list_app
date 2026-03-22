import tkinter as tk
from tkinter import messagebox
from logic.task_manager import *

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.geometry("450x550")
        self.root.configure(bg="#2c3e50")

        self.tasks = load_tasks()

        # Logo
        try:
            self.logo = tk.PhotoImage(file="assets/logo.png")
            tk.Label(root, image=self.logo, bg="#2c3e50").pack(pady=10)
        except:
            pass

        # Entry
        self.entry = tk.Entry(root, width=30, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task, width=20, bg="#27ae60", fg="white").pack(pady=5)
        tk.Button(root, text="Delete Task", command=self.delete_task, width=20, bg="#c0392b", fg="white").pack(pady=5)
        tk.Button(root, text="Mark Done", command=self.mark_done, width=20, bg="#2980b9", fg="white").pack(pady=5)

        # Listbox
        self.listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
        self.listbox.pack(pady=20)

        self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["done"]:
                self.listbox.insert(tk.END, "✔ " + task["task"])
            else:
                self.listbox.insert(tk.END, task["task"])

    def add_task(self):
        task = self.entry.get()
        if task:
            add_task(self.tasks, task)
            self.entry.delete(0, tk.END)
            self.tasks = load_tasks()
            self.update_list()
        else:
            messagebox.showwarning("Warning", "Enter a task")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            delete_task(self.tasks, index)
            self.tasks = load_tasks()
            self.update_list()
        except:
            messagebox.showwarning("Warning", "Select a task")

    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            mark_done(self.tasks, index)
            self.tasks = load_tasks()
            self.update_list()
        except:
            messagebox.showwarning("Warning", "Select a task")