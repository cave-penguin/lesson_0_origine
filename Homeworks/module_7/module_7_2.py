import os


# def custom_write(file_name, strings):
#     with open(file_name, 'w') as f:
#         pass
#     bytes_number = []
#     for string in strings:
#         file = open(file_name, 'r')
#         strings_in_file = file.read()
#         file.close()
#         file = open(file_name, "a")
#         if string not in strings_in_file:
#             bytes_number.append(file.tell())
#             file.write(f"{string}\n")
#         file.close()
#     file = open(file_name, "r")
#     strings_from_file = file.read().splitlines()
#     file.close()
#     positions = []
#     for string in strings_from_file:
#         if string:
#             positions.append(
#                 (
#                     strings_from_file.index(string) + 1,
#                     bytes_number[strings_from_file.index(string)],
#                 )
#             )
#     strings_positions = dict(zip(positions, strings_from_file))
#     return strings_positions


def custom_write(file_name, strings):
    positions = {}
    with open(file_name, "w", encoding="utf-8") as file:
        for index, string in enumerate(strings, 1):
            positions[(index, file.tell())] = string
            file.write(f"{string}\n")
    return positions


info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!",
]

result = custom_write("test.txt", info)
for elem in result.items():
    print(elem)
