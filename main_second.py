def remove_exclamation_marks(s):
    # return s.replace("!", "")
    new_s = ""
    for i in s:
        if i != "!" and i != "?" and i != "1":
            new_s += i
    return new_s


string = "Hi!!!!1!!????? Hello??!"


# print(remove_exclamation_marks(string))


def get_volume_of_cuboid(length, width, height):
    return length * width * height  # Code goes here...


# print(get_volume_of_cuboid(1, 2, 2))


def square_sum(numbers):
    sum_num = 0
    for i in numbers:
        square_num = i**2
        sum_num += square_num
    return sum_num


# print(square_sum([1, 2]))
def find_needle(haystack):
    # print(haystack.index("needle"))
    for i in range(0, len(haystack)):
        if haystack[i] == "needle":
            return f"found the needle at position {i}"
        else:
            i += 1


# print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))


# def double_char(s):
#     s2 = ""
#     for i in s:
#         s2 += i * 2
#     return s2


def double_char(s):
    return "".join(c * 2 for c in s)


# print(double_char("String"))


def remove_char(s):
    return s[1:-1]


# print(remove_char("eloquent"))
from datetime import date

current_datetime = date.today()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.weekday() + 1)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)

numbers = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
numbers_unique = list(dict.fromkeys(numbers))


# print(numbers_unique)


def bmi(weight, height):
    result = weight / height**2
    if result <= 18.5:
        return "Underweight"
    elif 18.5 < result <= 25.0:
        return "Normal"
    elif 25.0 < result <= 30.0:
        return "Overweight"
    else:
        return "Obese"


# print(bmi(400, 1.80))


def string_to_array(s):
    return s.split(" ")


# print(string_to_array("Robin Singh"))


def simple_multiplication(number):
    # if number % 2 == 0:
    #     return number * 8
    # if number % 2 != 0:
    #     return number * 9
    return number * (8 if number % 2 == 0 else 9)


# print(simple_multiplication(94321432145321))


def sum_no_duplicates(l):
    new = []
    for x in l:
        if l.count(x) == 1:
            new.append(x)
    return sum(new)


def sum_no_duplicates1(l):
    return sum(n for n in set(l) if l.count(n) == 1)


def sum_no_duplicates2(l):
    return sum([e for e in l if l.count(e) == 1])


# print(sum_no_duplicates2([3, 4, 3, 6]))


def reverse_words(text):
    split_string = text.split(" ")
    reversed_text = ""
    for word in split_string:
        reversed_string = "".join(reversed(word))
        reversed_text += reversed_string
    return reversed_text


# print(reverse_words("This is an example!"))


# a, b = 12, 65
# if a <= b:
#     print("yo")
# if a != b:
#     print("yo2")


# def descending_order(num):
#     return int("".join(sorted(str(num), reverse=True)))


# print(descending_order(123456789))


# def get_middle(s):
#     if len(s) % 2:
#         return s[len(s) // 2]
#     else:
#         return s[len(s) // 2 - 1 : len(s) // 2 + 1]


# print(get_middle("testq"))


# def DNA_strand(dna):
#     return "".join([{"A": "T", "T": "A", "C": "G", "G": "C"}[i] for i in dna])


# print(DNA_strand("ATTGC"))

# list_of_lists = [[1, 2], [3, 4], [1, 2], [5, 6], [3, 4]]

# unique_lists = []
# seen = set()

# for sublist in list_of_lists:
#     sublist_tuple = tuple(sublist)
#     if sublist_tuple not in seen:
#         unique_lists.append(list(sublist))
#         seen.add(sublist_tuple)

# print(unique_lists)


# num = int(input("Enter number: "))
#
# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")


# month = int(input("Enter num: "))

# match month:
#     case 1:
#         print("January")
#     case 2:
#         print("February")
#     case 3:
#         print("March")

# calls = 0
# def count_calls():
#     global calls
#     calls += 1
# count_calls()
# count_calls()
# count_calls()
# count_calls()
# print(calls)


# product_id = int(input('enter id: '))
# hex_product_id = hex(product_id)  # Перевод числа в шестнадцатеричную систему счисления
# octal_product_id = oct(product_id)  # Перевод числа в восьмеричную систему счисления
# binary_product_id = bin(product_id)  # Перевод числа в двоичную систему счисления
# print("HEX", hex_product_id[2:])
# print("OCT", octal_product_id[2:])
# print("BIN", binary_product_id[2:])


# shopping_list = ["Молоко", "Хлеб", "Яйца"]
# shopping_list_str = str(shopping_list)
# print(type(shopping_list_str))


# Задача: Создание координат точки на плоскости
# x_coord = 3
# y_coord = 5
# point_coordinates = tuple([x_coord, y_coord])
# print(point_coordinates)
# Теперь point_coordinates может быть использована, например, в качестве ключа в словаре или в множестве.


# Задача: Фильтрация уникальных тегов в блоге
# tags = ["Python", "JavaScript", "Python", "CSS"]
# unique_tags_set = set(tags)
# print(type(list(unique_tags_set)))
# Теперь unique_tags_set содержит уникальные теги без повторений для использования в блоге.


# print(str(2 + 2) * int("2" + "2"))


# str = "3.14, 42, True"
# lst = str.split(", ")
# num1 = float(lst[0])
# num2 = int(lst[1])
# bool1 = bool(lst[2])

# print(type(lst))
# print(type(num1))  # <class 'float'>
# print(type(num2))  # <class 'int'>
# print(type(bool1))  # <class 'bool'>

# def nat_num(n, res=''):
#     if n >= 1:
#         res += str(n) + ' '
#         return nat_num(n - 1, res)
#     return res

# print(nat_num(7))


# list_ = []


# def func(a, b):
#     if a <= b:
#         if a == b:
#             list_.append(str(b))
#         else:
#             list_.append(str(a))
#             func(a + 1, b)
#     elif b <= a:
#         if b == a:
#             list_.append(str(a))
#         else:
#             list_.append(str(b))
#             func(a, b + 1)

#     return " ".join(reversed(list_))


# print(func(2, 9))


# def transfer_str_nmb(string, nmb):
#     result = ['']
#     for char in string:
#         if len(result[-1]) < nmb:
#             result[-1] = result[-1] + char
#         else:
#             result.append(char)
#     return result

# # Example usage
# result = transfer_str_nmb("pythonstringexample", 5)
# print(result)


# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# my_list = [i for i in range(int(input('enter number: ')))]
# new_list = list(filter(lambda x: (x % 2 == 0), my_list))
# print(new_list)

# current_list = [i for i in range(int(input("enter number: ")))]
# # current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# new_list = list(map(lambda x: x ** 2, current_list))
# print(new_list)


# from functools import reduce


# current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
# summa = reduce((lambda x, y: x + y), current_list)
# print(summa)


# tables = [lambda x=x: x * 10 for x in range(1, 11)]
# for table in tables:
#     print(table(), end=" ")


# max_number = lambda a, b: a if a > b else b
# print(max_number(3, 5))


current_list = [[10, 6, 9], [0, 14, 16, 80], [8, 12, 30, 44]]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y) - 2] for y in func(x)]
result = second_largest(current_list, sorted_list)
# print(result)


def init():
    obj = {}
    arr = []

    class Builder:
        def setName(self, value1):
            obj["name"] = value1
            return self

        def setPrefix(self, value2):
            obj["prefix"] = value2
            return self

        def addAchievement(self, value3):
            arr.append(value3)
            obj["achievements"] = arr
            return self

        def getObject(self):
            if "achievements" in obj:
                return {
                    "name": obj["name"],
                    "prefix": obj["prefix"],
                    "achievements": obj["achievements"],
                }
            return {
                "name": obj["name"],
                "prefix": obj["prefix"],
            }

        def format(self):
            str = ", ".join(arr)
            return f"{obj['prefix']} {obj['name']} who {str}"

    return Builder()


# print(
#     init()
#     .setName("Vader")
#     .setPrefix("Darth")
#     .addAchievement("built Death Star")
#     .addAchievement("got a cookies")
#     .getObject()
# )
# print(
#     init()
#     .setName("Vader")
#     .setPrefix("Darth")
#     .addAchievement("built Death Star")
#     .addAchievement("got a cookies")
#     .format()
# )


#                                        Tic-Tac-Toe


# def print_board(board):
#     print("---------")
#     print("|", board[0], "|", board[1], "|", board[2], "|")
#     print("---------")
#     print("|", board[3], "|", board[4], "|", board[5], "|")
#     print("---------")
#     print("|", board[6], "|", board[7], "|", board[8], "|")
#     print("---------")
#
#
# def check_win(board, player):
#     # Check rows
#     for i in range(0, 9, 3):
#         if board[i] == board[i + 1] == board[i + 2] == player:
#             return True
#     # Check columns
#     for i in range(3):
#         if board[i] == board[i + 3] == board[i + 6] == player:
#             return True
#     # Check diagonals
#     if board[0] == board[4] == board[8] == player:
#         return True
#     if board[2] == board[4] == board[6] == player:
#         return True
#     return False
#
#
# def play_game():
#     board = [" "] * 9
#     player = "X"
#
#     while True:
#         print_board(board)
#         print("Player", player, "turn")
#         move = int(input("Enter move (0-8): "))
#         if board[move] == " ":
#             board[move] = player
#             if check_win(board, player):
#                 print_board(board)
#                 print("Player", player, "wins!")
#                 return
#             if " " not in board:
#                 print_board(board)
#                 print("It's a tie!")
#                 return
#             player = "O" if player == "X" else "X"
#         else:
#             print("Invalid move. Try again.")
#
#
# play_game()
def get_all_lists_or_dicts(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(get_all_lists_or_dicts(item))
        elif isinstance(item, dict):
            result.append(item)
    return result


a = {
    "a": 1,
    "b": 2,
    "c": {
        "d": 3,
        "e": 4,
        "f": {
            "g": 5,
            "h": 6,
        },
    },
}


def sum_lengths_and_numbers(data):
    total_length = 0
    total_numbers = 0

    if isinstance(data, dict):
        for key, value in data.items():
            total_length += len(key)
            if isinstance(value, str):
                total_length += len(value)
            elif isinstance(value, int):
                total_numbers += value
            else:
                subtotal_length, subtotal_numbers = sum_lengths_and_numbers(value)
                total_length += subtotal_length
                total_numbers += subtotal_numbers

    return total_length, total_numbers


# print(sum_lengths_and_numbers(a))


# Напишите функцию, которая принимает строку и возвращает true/false,
# если строка читается слева-направо, так же как справа-налево. Учитывать
# регистр, то есть программа должна одинаково реагировать на большие и маленькие буквы.
# Input: Abrarba
# Actions:
# Output: true
# Input: abraarba
# Actions:
# Output: true
# Input: abr1aarba
# Actions:
# Output: false


def is_palindrome(s):
    return s.lower() == s[::-1].lower()


def is_palindrome(s):
    s = s.lower()
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return s == reversed_s


# print(is_palindrome("Abrarba"))
# print(is_palindrome("abraarba"))
# print(is_palindrome("abr1aarba"))


# Напишите функцию, которая принимает строку и возвращает true/false, если строка читается слева-направо,
# так же как справа-налево, если при этом удалить или не удалять одну букву.
# Учитывать регистр, то есть программа должна одинаково реагировать на большие и маленькие буквы.
# Используйте предыдущее решение с рекурсией и функцией slice.
# Input: Abrar1ba
# Actions:
# Output: true
# Input: abraarba
# Actions:
# Output: true
# Input: abraa23rba
# Actions:
# Output: false


# Напишите функцию, возвращает, количество букв, которое надо удалить,
# чтобы слово читалось слева-направо, также как справа-налево.
# Учитывать регистр, то есть программа должна одинаково реагировать на большие и маленькие буквы.
# Используйте предыдущие решение, с рекурсией и функцией slice.
# Input: Abrar1ba
# Actions:
# Output: 1
# Input: Abrarba
# Actions:
# Output: 0
# Input: Abrar2341ba
# Actions:
# Output: 4
# print(...)
#
#
# def func():
#     return NotImplemented
#
#
# if func() is NotImplemented:
#     pass
#
#
# print(func())


# print("old" if int(input()) > 20 else "young")


import random

# Define possible operators
operators = ["+", "-", "*", "/"]

# Generate a list of valid expressions
expressions = []
for _ in range(200):
    # Randomly choose numbers with 1 to 3 digits
    num1 = str(random.randint(1, 999))
    num2 = str(random.randint(1, 999))
    operator = random.choice(operators)

    # Create a correct expression
    expression = f"{num1} {operator} {num2}"
    expressions.append(expression)

# Introduce errors in approximately 20% of expressions
error_indices = random.sample(range(200), int(0.2 * 200))
for index in error_indices:
    error_type = random.choice(["missing_element", "wrong_order"])
    if error_type == "missing_element":
        # Remove either one number or the operator randomly
        part_to_remove = random.choice([0, 1, 2])
        if part_to_remove == 0:  # remove the first number
            expressions[index] = expressions[index].split(" ", 1)[1]
        elif part_to_remove == 1:  # remove the operator
            parts = expressions[index].split(" ")
            expressions[index] = f"{parts[0]} {parts[2]}"
        else:  # remove the second number
            expressions[index] = expressions[index].rsplit(" ", 1)[0]
    else:
        # Swap the position of number and operator
        parts = expressions[index].split(" ")
        expressions[index] = f"{parts[1]} {parts[0]} {parts[2]}"

# Output the generated expressions
expressions[:10], len(expressions)  # Showing only the first 10 for brevity
