def greet_person(person_name):
    if person_name == "Volandemort":
        raise Exception("We dont love you, Volandemort")
    print(f"Hello, {person_name}!")


# greet_person("Dear student")
# greet_person("Volandemort")


# try:
#     raise NameError("Hello there!")
# except NameError as exc:
#     print(f"Type of exception {type(exc)} flew past! It parameters: {exc.args}")
#     raise


# class ProZero(Exception):
#     pass
#
#
# def f(a, b):
#     if b == 0:
#         raise ProZero("Деление на ноль невозможно")
#     return a / b


# print(f(10, 2))
# print(f(10, 0))


class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def f(a, b):
    if b == 0:
        raise ProZero("Деление на ноль невозможно", {"a": a, "b": b})
    return a / b


try:
    result = f(10, 0)
    print(result)
except ProZero as e:
    print("Не очень хороший день, мы словили ошибку ")
    print(f"Сообщения об ошибке: {e.message}")
    print(f"Дополнительная информация: {e.extra_info}")
