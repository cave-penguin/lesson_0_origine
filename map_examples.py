numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda num: num * 2, numbers))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]


strings = ["hello", "world", "how", "are", "you"]
capitalized_strings = list(map(str.upper, strings))
print(capitalized_strings)  # Output: ['HELLO', 'WORLD', 'HOW', 'ARE', 'YOU']


numbers = [1, 2, 3, 4, 5]
incremented_numbers = list(map(lambda num: num + 1, numbers))
print(incremented_numbers)  # Output: [2, 3, 4, 5, 6]


tuples = [(1, 2), (3, 4), (5, 6)]
sum_of_tuples = list(map(lambda s: sum(s), [*tuples]))
print(sum_of_tuples)  # Output: [3, 7, 11]


import time


def double_numbers_for_loop(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result


def double_numbers_map(numbers):
    return list(map(lambda num: num * 2, numbers))


numbers = [i for i in range(1000000)]

start_time = time.time()
result_for_loop = double_numbers_for_loop(numbers)
end_time = time.time()
print(f"Time taken for for loop: {end_time - start_time} seconds")

start_time = time.time()
result_map = double_numbers_map(numbers)
end_time = time.time()
print(f"Time taken for map: {end_time - start_time} seconds")
