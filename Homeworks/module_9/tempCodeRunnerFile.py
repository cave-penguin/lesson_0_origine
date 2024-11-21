def generate_combinations(s):
    for length in range(1, len(s) + 1):
        def combinations(current_combination="", index=0):
            if len(current_combination) == length:
                yield current_combination
                return
            for i in range(index, len(s)):
                yield from combinations(current_combination + s[i], i + 1)
        yield from combinations()


# Пример использования
s = "abcdefg"
combinations_generator = generate_combinations(s)

for combination in combinations_generator:
    print(combination)


def generate_combinations(s):
    for length in range(1, len(s) + 1):
        stack = [("", 0)]
        while stack:
            current_combination, index = stack.pop()
            if len(current_combination) == length:
                yield current_combination
            else:
                for i in range(index, len(s)):
                    stack.append((current_combination + s[i], i + 1))


# Пример использования
s = "abc"
combinations_generator = generate_combinations(s)

for combination in combinations_generator:
    print(combination)