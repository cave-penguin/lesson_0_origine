def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])


# print(solution(16))


def spin_words(sentence):
    return " ".join(
        ["".join(reversed(i)) if len(i) >
         4 else i for i in sentence.split(" ")]
    )


# print(spin_words("welcome"))


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# print(likes(["Alex"]))


def find_it(seq):
    return [i for i in seq if seq.count(i) % 2][0]


# print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


def digital_root(n):
    list_sum = sum([int(i) for i in str(n)])
    if list_sum < 10:
        return list_sum
    else:
        return digital_root(list_sum)


# print(digital_root(16))
# print(digital_root(942))
# print(digital_root(132189))
# print(digital_root(493193))

number = 12345
digits = [int(digit) for digit in str(number)]
# print(digits)


def create_phone_number(n):
    list_of_string = "".join([str(i) for i in n])
    return f"({list_of_string[:3]}) {list_of_string[3:6]}-{list_of_string[6:]}"
    # return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)


# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def count_bits(n):
    return sum([int(i) for i in str(bin(n)[2:])])


# print(count_bits(1234))


def move_zeros(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]


# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))


def pig_it(text):
    return " ".join([i[1:] + i[0] + "ay" if i.isalpha() else i for i in text.split()])


# print(pig_it("Hello world !"))


def make_readable(seconds):
    s = seconds % 60
    if s < 10:
        s = f"0{s}"
    else:
        s = f"{s}"
    m = (seconds // 60) % 60
    if m < 10:
        m = f"0{m}"
    else:
        m = f"{m}"
    h = (seconds // 60) // 60
    if h < 10:
        h = f"0{h}"
    else:
        h = f"{h}"
    return f"{h}:{m}:{s}"


# print(make_readable(59))


def rgb_to_hex(rgb):
    return "%02x%02x%02x" % rgb


# print(rgb_to_hex((255, 255, 255)))


def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


# print(rgb_to_hex(255, 255, 255))


def rgb(r, g, b):
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0

    return "{:02X}{:02X}{:02X}".format(r, g, b)


# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


# print(rgb(255, -255, 300))


def convert(base, value):
    if base == "dh":
        return hex(int(value))[2:]
    if base == "db":
        return bin(int(value))[2:]
    if base == "hd":
        return int(value, 16)
    if base == "bd":
        return int(value, 2)


def converter(a, b):
    if a == "dh":
        return hex(int(b))
    if a == "db":
        return bin(int(b))[2:]
    if a == "hd":
        return int(str(b), 16)
    if a == "bd":
        return int(str(b), 2)


# print(converter("db", "45"))


def zero(arg=None):
    return 0 if arg is None else int(arg(0))


def one(arg=None):
    return 1 if arg is None else int(arg(1))


def two(arg=None):
    return 2 if arg is None else int(arg(2))


def three(arg=None):
    return 3 if arg is None else int(arg(34))


def four(arg=None):
    return 4 if arg is None else int(arg(4))


def five(arg=None):
    return 5 if arg is None else int(arg(5))


def six(arg=None):
    return 6 if arg is None else int(arg(6))


def seven(arg=None):
    return 7 if arg is None else int(arg(7))


def eight(arg=None):
    return 8 if arg is None else int(arg(8))


def nine(arg=None):
    return 9 if arg is None else int(arg(9))


def plus(num):
    return lambda x: x + num


def minus(num):
    return lambda x: x - num


def times(num):
    return lambda x: x * num


def divided_by(num):
    return lambda x: x // num


# print(nine(divided_by(two())))


def f(n, s):
    return n ** (1 / s)


# print(f(9, 2))


def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap


year = int(input("Enter year: "))
print(is_leap(year))
print(1900 // 100)
