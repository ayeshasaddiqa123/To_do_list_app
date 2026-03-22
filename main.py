import tkinter as tk
from gui.app_ui import TodoApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()