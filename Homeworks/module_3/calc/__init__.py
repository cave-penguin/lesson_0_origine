import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, "end")
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title("Calculator")
window.geometry("260x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add.place(x=40, y=170)
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=90, y=170)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=140, y=170)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=190, y=170)
number1_entry = tk.Entry(window, width=21)
number1_entry.place(x=40, y=50)
number2_entry = tk.Entry(window, width=21)
number2_entry.place(x=40, y=120)
answer_entry = tk.Entry(window, width=22)
answer_entry.place(x=40, y=280)
number1 = tk.Label(window, text="Enter first number:")
number1.place(x=40, y=20)
number2 = tk.Label(window, text="Enter second number:")
number2.place(x=40, y=90)
answer = tk.Label(window, text="Result")
answer.place(x=40, y=250)
window.mainloop()
