import time

start_time = time.time()

my_numbers = [5, 3, 5, 6, 1, 8, 4, 9, 2]


result = [x**3000 for x in my_numbers]
print(result)


for elem in result:
    print(elem)


for elem in result:
    print(elem)


finish_time = time.time()

print(f"comprehension, time in milliseconds: {(finish_time - start_time) * 1000}")


start_time2 = time.time()

my_numbers = [5, 3, 5, 6, 1, 8, 4, 9, 2]


result = (x**3000 for x in my_numbers)
print(result)


for elem in result:
    print(elem)


for elem in result:
    print(elem)


finish_time2 = time.time()

print(f"generator, time in milliseconds: {(finish_time2 - start_time2) * 1000}")
