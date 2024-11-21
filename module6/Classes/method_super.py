class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f"My name is {self.name}")


class Student_Group:
    def __init__(self, group) -> None:
        self.group = group

    def about(self):
        print(f"{self.name} studies in group {self.group}")


class Student(Human, Student_Group):
    def __init__(self, name, place, group):
        super().__init__(name, group)
        self.place = place
        super().info()


# human = Human("Micky")
# print(human.name)
student = Student("Alex", "USA", "python 1")
# student.about()
print(Human.mro())
