class Human:
    head = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.say_info()

    def say_info(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")

    def birthday(self):
        self.age += 1
        print(f"{self.name} has been happy for {self.age} years")

    def __str__(self):
        return f"{self.name}"

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __bool__(self):
        return bool(self.age)

    # def __del__(self):
    #     print(f"{self.name} left.")


mick = Human("Micky", 42)
den = Human("Denis", 42)
den.head = False
print(Human.head)
print(den.__dict__)
