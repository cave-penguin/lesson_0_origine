list_1 = [1, 5, 9, 29, 4]
list_2 = [5, 2, 9, 1, 2]


ran = range(10, 30)
zp = zip(list_1, list_2)
mp = map(str, list_1)

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))
