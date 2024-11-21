# 1 task


class Soda:

    def __init__(self, supp=None):
        self.supp = supp

    def show_my_drink(self):
        if isinstance(self.supp, str):
            print(f"Газировка и {self.supp}")
        else:
            print("Обычная газировка")


# drink1 = Soda()
# drink2 = Soda("малина")
# drink3 = Soda(5)
# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()


# 2 task


class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return "Ура, можно построить треугольник!"
                return "Жаль, но из этого треугольник не сделать"
            return "С отрицательными числами ничего не выйдет!"
        return "Нужно вводить только числа!"


# Тесты
# triangle1 = TriangleChecker([2, 3, 4])
# print(triangle1.is_triangle())
# triangle2 = TriangleChecker([77, 3, 4])
# print(triangle2.is_triangle())
# triangle3 = TriangleChecker([77, 3, "Сторона3"])
# print(triangle3.is_triangle())
# triangle4 = TriangleChecker([77, -3, 4])
# print(triangle4.is_triangle())


# x = getattr(obj, "nm")  # возвращает атрибут
# print(x, 1)
#
# y = setattr(obj, "nm", "hello")  # меняет атрибут
# x = getattr(obj, "nm")  # возвращает атрибут
# print(x, 2)
#
# z = delattr(obj, "nm")
#
# m = hasattr(obj, "nm")
# print(m)

# 1. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. Напишите класс IceCreamStand,
# наследующий от класса Restaurant. Добавьте атрибут с именем flavors для хранения списка сортов мороженого.
# Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand и вызовите этот метод.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        long_name = f"{self.restaurant_name} - {self.cuisine_type}"
        print(long_name)

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, clients):
        self.number_served += clients


class IceCreamStand(Restaurant):
    def __init__(self, *flavors, restaurant_name=None, cuisine_type=None):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Сорта мороженого: ", ", ".join(self.flavors))


# ice_cream = IceCreamStand("Plombir", "Choclad", "Kaziabra")
# ice_cream.show_flavors()


class User:

    login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.login_attempts} попытка")

    def reset_login_attempts(self):
        self.login_attempts = 0

    def __init__(self, first_name, last_name, city, years):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.years = years

    def describe_user(self):
        print(
            f"Пользователь {self.first_name} {self.last_name}, {self.years} years old, from {self.city}"
        )

    def greet_user(self):
        print(f"Приветствую Вас, {self.first_name} {self.last_name}!")


class Admin(User):

    def __init__(self, first_name=None, last_name=None, city=None, years=None):
        super().__init__(first_name, last_name, city, years)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = [
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей",
        ]

    def show_privileges(self):
        print(f"Привилегии администратора: {', '.join(self.privileges)}.")


# admin = Admin()
# admin.privileges.show_privileges()


# 2. Администратор: администратор — особая разновидность пользователя. Напишите
# класс с именем Admin, наследующий от класса User. Добавьте атрибут privileges для хранения списка строк вида
# "разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей" и т. д.
# Напишите метод show_privileges() для вывода набора привилегий администратора.
# Создайте экземпляр Admin и вызовите свой метод.

# 3. Привилегии: напишите класс Privileges. Класс должен содержать всего один атрибут privileges со списком строк.
# Переместите метод show_privileges() в этот класс. Создайте экземпляр Privileges как атрибут класса Admin.
# Создайте новый экземпляр Admin и используйте свой метод для вывода списка привилегий.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Название: {self.title}, Автор: {self.author}, Год издания: {self.year}"


class Library(Book):
    def __init__(self):

        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("Library is empty")


# Создание экземпляров книг
# book1 = Book("1984", "George Orwell", 1949)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
#
# # Создание библиотеки
# library = Library()
#
# # Добавление книг в библиотеку
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# # Отображение всех книг
# library.display_books()
#
# # Поиск книги
# found_book = library.find_book("1984")
# if found_book:
#     print(f"\nНайдена книга: {found_book}")
#
# # Удаление книги
# library.remove_book("1984")
#
# # Повторное отображение всех книг
# library.display_books()
