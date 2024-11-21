# from tkinter import *
# from tkinter import ttk

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
# import tkinter as tk
#
# root = tk.Tk()
#
# label = tk.Label(root, text="Это метка")
# label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
#
# button = tk.Button(root, text="Это кнопка")
# button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
#
# root.mainloop()
# import tkinter as tk
#
# root = tk.Tk()
#
# label = tk.Label(root, text="Это метка")
# label.pack()
#
# button = tk.Button(root, text="Изменить метку")
# button.pack()
#
#
# def change_label():
#     label.configure(text="Новый текст", fg="red", font=("Arial", 12))
#
#
# button.configure(command=change_label)
#
# root.mainloop()
import tkinter as tk

window = tk.Tk()

window.configure(
    title="Мое окно",
    geometry="800x600",
    resizable=(True, True),
    minsize=(400, 300),
    maxsize=(1024, 768),
    background="#f0f0f0",
    highlightbackground="#ccc",
    highlightthickness=2,
    iconify=True,
    state="normal",
)

window.mainloop()
