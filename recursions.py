# def rec(n):
#     if n == 1:
#         return 1
#     else:
#         return n + rec(n - 1)
#
#
# print(rec(100))


# def rec1(n):
#     if len(n) <= 1:
#         return n
#     else:
#         return rec1(n[1:]) + n[0]
# def rec1(n):
#     return n[::-1]
#
#
# print(rec1("abcdefghijklmnopqrsuvwxyz"))
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))


# def summ(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + summ(n // 10)
#
#
# print(summ(12345454325454532543253543255353253535325432535325))


# def is_palindrom(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] == s[-1]:
#         return is_palindrom(s[1:-1])
#     else:
#         return False
#
#
# print(is_palindrom("qwertyytrewq"))

#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(7))


# def square(n, x):
#     if x == 0:
#         return 1
#     else:
#         return n * square(n, x - 1)
#
#
# print(square(2, 5))
# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return max(lst[0], find_max(lst[1:]))
#
#
# print(find_max([4, 2, 4, 5, 63, 1, 8, 9, 7, 6, 5, 98, 4, 212, 434]))
