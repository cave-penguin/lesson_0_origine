# try:
#     a = 10
#     x = 0
#     print(a / x)
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")

# try:
#     truba = a + b
#     truba = 10 / 0
# except (ZeroDivisionError, NameError):
#     print("something went wrong, but we did it!")


# try:
#     truba = a + b
#     truba = 10 / 0
# except ZeroDivisionError:
#     print("you can't divide by zero!")
# except NameError:
#     print("a and b must be defined")

# try:
#     a = 10 / 0
# except ZeroDivisionError as exc:
#     print(f"Error: {exc}!")


# try:
#     file = open("something.txt")
# except OSError as exc:
#     print(f"Error: {exc}, parameters {exc.args}!")


# try:
#     a = 10 / 0
#     print(round(a, 2))
# except ZeroDivisionError:
#     print("Error: can't divide by zero!")
# else:
#     print("Everything is ok, all is well!")
# finally:
#     print("The 'try except' is finished!")


# print("----- Какой хороший день, предлагаю научиться работать с исключениями  -----")
# i = int(input("Введи целое число: "))


# try:
#     result = 10 * (1 / i)
# except ZeroDivisionError as exc:
#     print(f"Нельзя делить на ноль: {exc}")
# else:
#     print(f"Ура, мы не делим на ноль {round(result, 2)}")
# finally:
#     print("Конец программы")


# def f1(number):
#     return 10 / number
#
#
# def f2():
#     print("What an awesome day!")
#     result_f1 = f1(0)
#     return result_f1
#
#
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print("You cannot divide by zero!", exc)


# def f1(number):
#     return 10 / number


# def f2():
#     print("What an awesome day!")
#     summ = 0
#     for i in range(-2, 2, 1):
#         try:
#             summ += f1(i)
#             print(summ)
#         except ZeroDivisionError as exc:
#             print(
#                 f"Inside f1 something goes wrong: {exc} but program is life, We are great!"
#             )
#     return summ / 0
#
#
# try:
#     total = f2()
#     print(f"Here is the result of your function: {total}")
# except ZeroDivisionError as exc:
#     print(f"Inside f2 something goes wrong: {exc} but We did it!")


# def f1(number):
#     return total / number
#
#
# def f2():
#     print("What an awesome day!")
#     summ = 0
#     for i in range(-2, 2, 1):
#         try:
#             summ += f1(i)
#             print(summ)
#         except ZeroDivisionError as exc:
#             print(
#                 f"Inside f1 something goes wrong: {exc} but program is life, We are great!"
#             )
#     return summ / 0
#
#
# try:
#     f2()
# except NameError as exc:
#     print(f"Inside f2 something goes wrong: {exc} but We did it!")
