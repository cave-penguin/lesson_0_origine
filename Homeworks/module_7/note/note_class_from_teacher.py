import tkinter as tk
from tkinter import messagebox, filedialog


window = tk.Tk()
window.geometry("300x300")
window.title("Note")

menubar = tk.Menu(window)
window.config(menu=menubar)


class Note:

    def __init__(self):
        self.is_saved = {"saved": False, "filename": ""}
        self.text_field = tk.Text(window, wrap=tk.WORD)
        self.text_field.configure(bg="lightblue", fg="black")
        self.text_field.pack(fill=tk.BOTH, expand=True)

    def new_file(self):
        if self.text_field.get("1.0", "end-1c").strip():
            response = messagebox.askyesno("Save", "Do you want to save changes?")
            if response:
                self.save_file()

        self.text_field.delete("1.0", "end")
        self.is_saved["saved"] = False
        self.is_saved["filename"] = ""

    def open_file(self):
        if self.text_field.get("1.0", "end-1c").strip():
            response = messagebox.askyesno("Save", "Do you want to save changes?")
            if response:
                self.save_file()
        filename = filedialog.askopenfilename()
        if filename:
            with open(filename, "r", encoding="utf-8") as file:
                file_content = file.read()
                self.text_field.delete("1.0", "end")
                self.text_field.insert("1.0", file_content)
                self.is_saved["saved"] = True
                self.is_saved["filename"] = filename

    def save_file(self):
        if self.is_saved["saved"]:
            with open(self.is_saved["filename"], "w") as file:
                file.write(self.text_field.get("1.0", "end-1c"))
        else:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text files", "*.txt")]
            )
            if filename:
                with open(filename, "w") as file:
                    file.write(self.text_field.get("1.0", "end-1c"))
                    self.is_saved["saved"] = True
                    self.is_saved["filename"] = filename

    def exit_program(self):
        if self.text_field.get("1.0", "end-1c").strip():
            response = messagebox.askyesno("Save", "Do you want to save changes?")
            if response:
                self.save_file()
        window.destroy()


note = Note()
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=note.new_file)
filemenu.add_command(label="Open", command=note.open_file)
filemenu.add_command(label="Save", command=note.save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=note.exit_program)
window.protocol("WM_DELETE_WINDOW", note.exit_program)

window.mainloop()
