import io
from pprint import pprint


name = "sample2.txt"

with open(name) as file:
    for line in file:
        for char in line:
            print(char, end="")
    print(file.tell())

# delete /n in end of line in file with readlines()
journal = [line.strip() for line in file.readlines()]
journal = list(map(str.strip, file.readlines()))
journal = list(map(lambda line: line.strip(), file.readlines()))
