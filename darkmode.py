import tkinter as tk

def toggle_dark_mode():
    if theme.get() == "dark":
        root.configure(bg="black")
        label.configure(fg="white")
    else:
        root.configure(bg="white")
        label.configure(fg="black")

root = tk.Tk()
theme = tk.StringVar(value="light")
tk.Radiobutton(root, text="Light", variable=theme, value="light", command=toggle_dark_mode).pack()
tk.Radiobutton(root, text="Dark", variable=theme, value="dark", command=toggle_dark_mode).pack()
label = tk.Label(root, text="Hello, World!")
label.pack()
root.mainloop()
