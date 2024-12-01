a = "Hello"
chars = []

for i in a:
    chars.append(ord(i))

s = ""
for i in chars:
    s += chr(i)

# print(chars)
# print(s)

# for i in range(1000, 1200):
#     print(chr(i), end=" ")

print(hex(ord("h")))

bb = b"\x68"

print(bb.decode())

# Виктория Маркова
# 19:41
# Sample Input 1:
# 1
# bwfusvfupdbftbs
# Sample Output 1:
# avetruetocaesar
# Виктория Маркова
# 19:45


n = int(input())
s = input()
for i in s:
    code = ord(i) - n
    if code < 97:
        code = code + 26
    new_i = chr(code)
    print(new_i, end="")

for el in s:
    cur_n = ord("a") + (ord(el) - ord("a") + 26 - n) % 26
    print(chr(cur_n), end="")


alphabet = "abcdefghijklmnopqrstuvwxyz"

for c in s:
    ind = alphabet.index(c)
    new_c = alphabet[ind - n]
    print(new_c, end="")
