my_list = []
for i in range(1, 1_000_001):
    my_list.append(i)


print(min(my_list))
print(max(my_list))
print(sum(my_list))


for i in range(1, 21, 2):
    print(i)


my_list = [i for i in range(1, 31) if i % 3 == 0]
for i in my_list:
    print(i)

cubes = [i**3 for i in range(1, 11)]
for i in cubes:
    print(i)
