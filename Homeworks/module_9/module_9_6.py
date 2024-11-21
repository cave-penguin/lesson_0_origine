

# def all_variants(text):
#     for length in range(1, len(text) + 1):
#
#         def func(x="", index=0):
#             if length == len(x):
#                 yield x
#             else:
#                 for i in range(index, len(text)):
#                     yield from func(x + text[i], i + 1)
#
#         yield from func()


# def all_variants(text):
#     for length in range(1, len(text) + 1):
#         x = ""
#         index = 0
#         for i in range(index, len(text)):
#             if len(x) != length:
#                 x += text[i]
#                 index += 1
#             elif len(x) == length and index == length:
#                 yield x
#
#
# a = all_variants("abc")
# for i in a:
#     print(i)


# from itertools import combinations, chain

# s = "abc"

# Генерируем все комбинации разной длины (от 1 до длины строки)
# combinations_result = list(
#     chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))
# )
#
# Преобразуем каждую комбинацию в строку и выводим результат
# for combination in combinations_result:
#     print("".join(combination))


# def generate_combinations(s):
#     for length in range(1, len(s) + 1):
#         def combinations(current_combination="", index=0):
#             if len(current_combination) == length:
#                 yield current_combination
#                 return
#             for i in range(index, len(s)):
#                 yield from combinations(current_combination + s[i], i + 1)
#         yield from combinations()
#
#
# # Пример использования
# s = "abc"
# combinations_generator = generate_combinations(s)
#
# for combination in combinations_generator:
#     print(combination)
#
#
# def generate_combinations(s):
#     for length in range(1, len(s) + 1):
#         stack = [("", 0)]
#         while stack:
#             current_combination, index = stack.pop()
#             if len(current_combination) == length:
#                 yield current_combination
#             else:
#                 for i in range(index, len(s)):
#                     stack.append((current_combination + s[i], i + 1))
#
#
# # Пример использования
# s = "abc"
# combinations_generator = generate_combinations(s)
#
# for combination in combinations_generator:
#     print(combination)


def all_variants(text):
    for length in range(1, len(text) + 1):
        for i in range(len(text) - length + 1):
            yield text[i : i + length]


# Пример использования
a = all_variants("abc")
for i in a:
    print(i)


# def generate_combinations(s):
#     for length in range(1, len(s) + 1):
#         for i in range(len(s) - length + 1):
#             yield "".join(s[j] for j in range(i, i + length))
#
#
# # Пример использования
# s = "abc"
# for combination in generate_combinations(s):
#     print(combination)
