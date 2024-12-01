from pprint import pprint
import sys


# pprint(dir(sys))

# print(sys.executable)

# print(sys.platform)

# print(sys.version[0:7])
# print(sys.version_info)


# def func(x):
# 	if sys.version.split(' ')[0] == '3.12.0':
# 		return x + 10
# 	else:
# 		raise Exception('Wrong version')
	
# print(func(10))


# print(sys.argv)

# print(sys.path)

# print(sys.modules)

# print(__builtins__)

# pprint(dir(__builtins__))

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)

sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(10000)
print(factorial(2000))
print(sys.getsizeof(factorial))
