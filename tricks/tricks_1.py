"""1. Использование get() с функцией по умолчанию
Вместо громоздких проверок if или try-except, можно использовать get() с лямбдой по умолчанию в словарях. Это позволяет динамически выбирать поведение.
"""

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Division by zero",
}
operator = "*"
num1 = 4
num2 = 9
result = operations.get(operator, lambda x, y: "Unknown operation")(num1, num2)
print(result)


"""2. Использование enumerate() для итерации со счётчиком
Для лучшего понимания и краткости кода вместо range(len(list)) лучше использовать enumerate(). Это делает код чище и избавляет от риска выхода за границы списка."""
my_list = [1, 2, 3, 4, 5]

for index, value in enumerate(my_list):
    print(f"{index}: {value}")


"""3. Декораторы для повторного использования логики
Сеньор-разработчики часто создают свои декораторы, чтобы добавить к функциям универсальное поведение — например, логирование, кэширование или валидацию данных. Это делает код более модульным и переиспользуемым."""

from functools import wraps


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log_execution
def my_function(x, y):
    return x + y


# Вывод: "Executing my_function with (2, 3) and {}"
my_function(2, 3)


"""4. Использование contextlib.contextmanager для чистого управления ресурсами
Для случаев, когда нужен собственный менеджер контекста (например, для открытия и закрытия соединений или файлов), используется @contextmanager из contextlib. Это позволяет управлять ресурсами чисто и эффективно, избегая ошибок."""

from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()


with open_file("test.txt", "w") as file:
    file.write("Hello, World!")


"""5. Использование collections.defaultdict для удобной работы со словарями
defaultdict автоматически инициализирует значения, что устраняет необходимость в проверках перед доступом к ключам."""

from collections import defaultdict

words = {"1": 1, "2": 2, "3": 3, "1": 1}

counter = defaultdict(int)
for word in words:
    counter[word] += 1  # Не нужно проверять, есть ли слово в словаре

# print(counter)

"""7. Понимание и использование конструкций *args и **kwargs
*args и **kwargs делают функции более гибкими. Опытные разработчики используют их, чтобы обрабатывать любое количество позиционных и именованных аргументов, что полезно при создании универсальных функций и методов."""


def flexible_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


flexible_function(1, 2, 3, [1, 2], name="Alice", age=25)


"""8. Списочные выражения и генераторы
Сеньоры часто используют списочные выражения и генераторы для лаконичного создания списков, множеств и словарей — это делает код более компактным и эффективным."""

squares = [x**2 for x in range(10)]
even_squares = (x**2 for x in range(10) if x % 2 == 0)
print(squares)
print([i for i in even_squares])


"""9. Использование параметров по умолчанию с изменяемыми типами данных
Избегайте изменяемых типов данных как значений по умолчанию в аргументах функций. Опытные разработчики создают экземпляр изменяемого объекта внутри функции, если он не передан явно."""


def append_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


"""10. Логирование вместо print()
Сеньоры используют модуль logging вместо print() для вывода в консоль, так как logging позволяет легко контролировать уровень важности сообщений и хранить логи."""


import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an informational message.")
logging.error("This is an error message.")
