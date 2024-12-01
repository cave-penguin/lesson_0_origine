import tkinter as tk
from tkinter import messagebox, filedialog

window = tk.Tk()
window.geometry("300x300")
window.title("Note")

is_saved = {"saved": False, "filename": ""}


def new_file():
    global is_saved
    if text_field.get("1.0", "end").strip() and not is_saved["saved"]:
        response = messagebox.askyesno("Save", "Do you want to save changes?")
        if response:
            save_file()
            text_field.delete("1.0", "end")
            is_saved["saved"] = False
            is_saved["filename"] = ""
        else:
            text_field.delete("1.0", "end")
            is_saved["saved"] = False
            is_saved["filename"] = ""
    elif text_field.get("1.0", "end").strip() and is_saved["saved"]:
        with open(is_saved["filename"], "w") as file:
            file.write(text_field.get("1.0", "end"))
            text_field.delete("1.0", "end")
            is_saved["saved"] = False
            is_saved["filename"] = ""


def open_file():
    if text_field.get("1.0", "end").strip():
        save_file()
    else:
        with open(filedialog.askopenfilename(), "r") as file:
            file_content = file.read()
            text_field.insert("1.0", file_content)
            is_saved["saved"] = True
            is_saved["filename"] = file.name


def save_file():
    global is_saved
    if not is_saved["saved"]:
        filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if filename:
            with open(filename, "w") as file:
                file.write(text_field.get("1.0", "end"))
                is_saved["saved"] = True
                is_saved["filename"] = file.name
    else:
        with open(is_saved["filename"], "w") as file:
            file.write(text_field.get("1.0", "end"))


def exit_program():
    new_file()
    window.destroy()


menubar = tk.Menu(window)
window.config(menu=menubar)

filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_program)

text_field = tk.Text(window, wrap=tk.WORD)
text_field.configure(bg="lightblue", fg="black")
text_field.pack(fill=tk.BOTH, expand=True)
text_field.pack()

window.mainloop()
