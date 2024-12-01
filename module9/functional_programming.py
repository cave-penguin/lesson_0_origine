# def get_russian_names():
#     return ["Ваня", "Коля", "Петя"]


# print(get_russian_names.__name__)


# my_func = get_russian_names


# print(my_func())
# print(my_func.__name__)


# def get_russian_names():
#     return ["Ваня", "Коля", "Петя"]
#
#
# def get_british_names():
#     return ["Fred", "Wilma", "Pebbles"]
#
#
# name_getters = [get_russian_names, get_british_names]
#
# for name_getter in name_getters:
#     print(name_getter())


def adder(args):
    res = 0
    for number in args:
        res += number
    return res


def multiplier(args):
    res = 1
    for number in args:
        res *= number
    return res


def process_numbers(numbers, function):
    result = function(numbers)
    print(f"Получилось {result}")


# my_numbers = [6, 2, 4, 8, 5, 1, 3, 7]

# process_numbers(numbers=my_numbers, function=adder)
# process_numbers(numbers=my_numbers, function=multiplier)


# def mul_by_2(x):
#     return x * 2
#
#
# my_numbers = [6, 2, 4, 8, 5, 1, 3, 7]
#
# result = map(mul_by_2, my_numbers)
#
# print(result)
# print(list(result))


def is_odd(x):
    return x % 2


my_numbers = [6, 2, 4, 8, 5, 1, 3, 7]

result = filter(is_odd, my_numbers)

print(result)
print(list(result))
