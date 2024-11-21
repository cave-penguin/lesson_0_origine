# import queue
# from random import randint
# from threading import Thread, Lock
# from time import sleep


# class Table:
#     def __init__(self, number):
#         self.number: int = number
#         self.guest = None


# class Guest(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name: str = name

#     def run(self):
#         wait = randint(3, 10)
#         sleep(wait)
#         print("unblock")


# class Cafe:
#     def __init__(self, *tables):
#         self.q = queue.Queue()
#         self.tables = tables
#         self.lock = Lock()

#     def guest_arrival(self, *guests):
#         for g in guests:
#             with self.lock:
#                 available_tables = [
#                     table for table in self.tables if table.guest is None
#                 ]
#                 if available_tables:
#                     print("block")
#                     table = available_tables.pop(0)
#                     table.guest = g
#                     g.start()
#                     print(f"{g.name} сел(-а) за стол номер {table.number}")
#                 else:
#                     self.q.put(g)
#                     print(f"{g.name} в очереди")

#     def discuss_guests(self):
#         while True:
#             with self.lock:
#                 for table in self.tables:
#                     if table.guest and not table.guest.is_alive():
#                         print("block")
#                         print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
#                         print(f"Стол номер {table.number} свободен")
#                         table.guest = None
#                     if table.guest is None and not self.q.empty():
#                         next_guest = self.q.get()
#                         table.guest = next_guest
#                         print(
#                             f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер "
#                             f"{table.number}"
#                         )
#                         next_guest.start()
#             if self.q.empty() and all(table.guest is None for table in self.tables):
#                 break


# # Создание столов
# tables = [Table(number) for number in range(1, 6)]
# # Имена гостей
# guests_names = [
#     "Maria",
#     "Oleg",
#     "Vakhtang",
#     "Sergey",
#     "Darya",
#     "Arman",
#     "Vitoria",
#     "Nikita",
#     "Galina",
#     "Pavel",
#     "Ilya",
#     "Alexandra",
# ]
# # Создание гостей
# guests = [Guest(name) for name in guests_names]
# # Заполнение кафе столами
# cafe = Cafe(*tables)
# # Приём гостей
# cafe.guest_arrival(*guests)
# # Обслуживание гостей
# cafe.discuss_guests()


import queue
from random import randint
from threading import Thread, Lock
from time import sleep


class Table:
	"""
	Класс, представляющий стол в кафе.

	Attributes:
		number (int): Номер стола.
		guest (Guest): Гость, занимающий стол (изначально None).
	"""

	def __init__(self, number: int):
		"""
		Инициализация стола с номером.

		Args:	
			number (int): Номер стола.
		"""
		self.number: int = number
		self.guest = None


class Guest(Thread):
	"""
	Класс, представляющий гостя кафе, наследующийся от потока.

	Attributes:
		name (str): Имя гостя.
	"""

	def __init__(self, name: str):
		"""
		Инициализация гостя с именем.

		Args:
			name (str): Имя гостя.
		"""
		super().__init__()
		self.name: str = name

	def run(self):
		"""
		Симуляция процесса пребывания гостя за столом.
		Гость "сидит" за столом случайное количество времени (от 3 до 10 секунд),
		затем освобождает стол.
		"""
		wait = randint(3, 10)
		sleep(wait)


class Cafe:
	"""
	Класс, представляющий кафе с несколькими столами и гостями.

	Attributes:
		q (queue.Queue): Очередь для гостей, ожидающих свободного стола.
		tables (list): Список столов.
		lock (Lock): Мьютекс для синхронизации доступа к столам.
	"""

	def __init__(self, *tables: Table):
		"""
		Инициализация кафе со столами.

		Args:
			*tables (Table): Переменное количество объектов Table.
		"""
		self.q = queue.Queue()
		self.tables = tables
		self.lock = Lock()

	def guest_arrival(self, *guests: Guest):
		"""
		Принимает гостей, рассаживает их за столы или добавляет в очередь.

		Args:
			*guests (Guest): Переменное количество объектов Guest.
		"""
		for g in guests:
			with self.lock:
				available_tables = [
					table for table in self.tables if table.guest is None
				]
				if available_tables:
					table = available_tables.pop(0)
					table.guest = g
					g.start()
					print(f"{g.name} сел(-а) за стол номер {table.number}")
				else:
					self.q.put(g)
					print(f"{g.name} в очереди")

	def discuss_guests(self):
		"""
		Обслуживает гостей, следит за освобождением столов и рассаживанием гостей из очереди.
		Выполняется, пока все гости не обслужены и все столы не освободятся.
		"""
		while True:
			with self.lock:
				for table in self.tables:
					if table.guest and not table.guest.is_alive():
						print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
						print(f"Стол номер {table.number} свободен")
						table.guest = None
					if table.guest is None and not self.q.empty():
						next_guest = self.q.get()
						table.guest = next_guest
						print(
							f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер "
							f"{table.number}"
						)
						next_guest.start()
			if self.q.empty() and all(table.guest is None for table in self.tables):
				break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
	"Maria", "Oleg", "Vakhtang", "Sergey", "Darya", "Arman",
	"Vitoria", "Nikita", "Galina", "Pavel", "Ilya", "Alexandra",
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
