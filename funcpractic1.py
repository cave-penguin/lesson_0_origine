def find_max(list_: list) -> int:
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i

    return max_


# print(find_max([1, 4, 3, 2, 2, 4, 3, 4, 3, 2, 5]))


# import random


# def count_even(list_):
#     counter = 0
#     for i in list_:
#         if i == 0:
#             continue
#         if i % 2 == 0:
#             counter += 1
#     return counter


# a = int(input("Enter Number: "))
#
# b = []
# for i in range(a):
#     b.append(random.choice([i for i in range(0, 99)]))


# print(b)
# print(count_even(b))


def unique(list_: list) -> list:
    new_list: list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(unique([1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 1]))
