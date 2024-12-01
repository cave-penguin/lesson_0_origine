import inspect
from pprint import pprint
import requests

some_string = "I am a string"
some_number = 42
some_list = [some_string, some_number]


def some_function(param, param_2="n/a"):
    print("my params is", param, param_2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()

func = some_function

# print(some_function.__name__)
# print(SomeClass.__name__)
# print(requests.__name__)
# print(func.__name__)


# AttributeError: 'str' object has no attribute '__name__'. Did you mean: '__ne__'?
# print(some_string.__name__)
# print(some_number.__name__)

# print(type(some_number))
# print(type(some_number) is int)
# print(type(some_number) is list)

# print(type(requests))
# print(type(requests.get))


# pprint(dir(some_number))
# pprint(dir(some_list))
# pprint(dir(some_function))
# pprint(dir(SomeClass))
# pprint(dir(some_object))
# pprint(dir(requests))


# pprint(dir())


# attr_name = 'attribute_2'
# print(hasattr(some_object, attr_name))
# print(hasattr(some_object, 'attribute_1'))

# def func():
#     return 'Wrong attribute'

print(getattr(some_object, 'attribute_1'))
print(getattr(some_object, 'attribute_2', func()))

# for attr_name in dir(requests):
#     attr = getattr(requests, attr_name)
#     print(attr_name, type(attr))


# print(callable(some_string))
# print(callable(some_function))
# print(callable(some_object.attribute_1))
# print(callable(some_object.some_class_method))


# print(isinstance(some_number, str))
# print(isinstance(some_number, int))
# print(isinstance(some_number, SomeClass))
# print(isinstance(some_object, SomeClass))


# print(inspect.ismodule(requests))
# print(inspect.ismodule(some_object))
# print(inspect.isclass(requests))
# print(inspect.isfunction(requests))
# print(inspect.isbuiltin(requests))

some_function_module = inspect.getmodule(SomeClass)
print(type(some_function_module), some_function_module)