import tkinter as tk

root = tk.Tk()
root.title("Hello")
root.geometry("300x120")
root.resizable(False, False)

tk.Label(
    root,
    text="Hello!",
    font=("Segoe UI", 18)
).pack(expand=True)

root.after(5000, root.destroy)
root.mainloop()