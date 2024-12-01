class User:
    __instanse = None

    def __new__(cls, *args, **kwargs):
        # print("Im in new.")
        if cls.__instanse is None:
            cls.__instanse = super().__new__(cls)
        return cls.__instanse

    def __init__(self, *args, **kwargs):
        # print("Im in init.")
        self.args = args
        # for i in args:
        #     setattr(self, "args", i)
        for key, value in kwargs.items():
            setattr(self, key, value)
        

other = [23, 32, 43]
user = {"name": "Denis", "age": 33, "gender": "male"}


user1 = User(*other, **user)
# print(user1.args)
# print(user1.name)
# print(user1.age)
# print(user1.gender)

print(user1.args[0])


# class Point:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         # print('Вызов __new__ для ' + str(cls))
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
        
#     def __init__(self, x=0, y=0):
#         # print('Вызов __init__ для ' + str(self))
#         self.x = x
#         self.y = y
        
#     def sum(self):
#         return self.x + self.y
        
        
# pt = Point(1, 2)
# pt1 = Point(3, 4)   
# pt2 = Point(5, 6)
# print(pt1.sum())
# print(pt2.sum())
# print(pt.sum())