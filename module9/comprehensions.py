def by_3(x):
    return x * 3


def is_odd(x):
    return x % 2


my_numbers = [3, 5, 1, 3, 4, 7, 6, 8, 9, 2, 1, 5, 6]


result = map(by_3, filter(is_odd, my_numbers))


# print(list(result))


#  List comprehension
# list_comp_1 = [x * 2 for x in collection]


result = [x * 3 for x in my_numbers]
# result = list(map(lambda x: x * 3, my_numbers))
# print(result)


# list_comp_2 = [x*2 for x in collection if x > 5]


result = [x * 3 for x in my_numbers if x % 2]
# result = list(map(lambda x: x * 3, list(filter(lambda x: x % 2, my_numbers))))
# print(result)


# list_comp_3 = [x * 2 if x > 2 else x * 10 for x in collection]


my_numbers = ["A", 4, 2, "B", 9, "C", 6, 1]

result = [x if isinstance(x, str) else x * 5 for x in my_numbers]
# print(result)


# list_comp_4 = [x * y for x in collection for y in collection_2]


my_numbers = [1, 4, 2, 6, 5, 7, 8, 9, 5, 3]
they_numbers = [1, 8, 5, 3, 2, 4, 6, 5, 2, 9]

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

result = [x * y for x in my_numbers for y in they_numbers]
# print(result)

result2 = [x * y for x in my_numbers for y in they_numbers if x % 2]
# print(result2)

result3 = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
# print(result3)


result = {x for x in my_numbers}
# print(result)

result2 = {x: x**2 for x in my_numbers}
# print(result2)
