# def func_generator(n):
#     i = 0
#     while i != n:
#         yield i
#         i += 1
#
#
# obj = func_generator(10)
# print(obj)
#
# for i in obj:
#     print(i)


# def fibonacci_v1(n):
#     result = []
#     a, b = 0, 1
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result
#
#
# def fibonacci_v2(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b


# fib_1 = fibonacci_v1(n=10)
# print(fib_1)
#
# for value in fib_1:
#     print(value)

# fib_2 = fibonacci_v2(n=10)
# print(fib_2)
#
# for value in fib_2:
#     print(value)


# def fibonacci_v3():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# for value in fibonacci_v3():
#     print(value)
#     if value > 100**6:
#         break


# import time
#
# start = time.time()
#
#
# def read_large_file(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()
#
#
# for line in read_large_file("large_file.txt"):
#     print(line)
#
#
# end = time.time()

# print((end - start) * 1000)


# def triangle_numbers():
#     n = 1
#     while True:
#         res = (n * (n + 1)) / 2
#         yield int(res)
#         n += 1
#
#
# result = triangle_numbers()
# for i in range(1, 1001):
#     print(next(result))


# def fibonacci():
#     m, n = 0, 1
#     while True:
#         yield m
#         m, n = n, m + n
#
#
# limit = 50
# result = fibonacci()
# for i in range(1, limit + 1):
#     print(next(result))


# def prime_numbers():
#     counter = 2  # Начинаем с первого простого числа
#     while True:
#         is_prime = True
#         for i in range(2, int(counter**0.5) + 1):
#             if counter % i == 0:  # Если делится без остатка, это не простое число
#                 is_prime = False
#                 break
#         if is_prime:
#             yield counter  # Число простое, возвращаем его
#         counter += 1
#
#
# limit = 100000
#
# result = prime_numbers()
# for i in range(limit):
#     print(next(result))
