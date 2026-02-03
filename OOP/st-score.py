class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.grade = "N/A"

    def calculate_grade(self):

        if self.marks > 400:
            self.grade = "A"
        elif self.marks > 350:
            self.grade = "B"
        else:
            self.grade = "C"


john = Student("John", 20, 450)
john.calculate_grade()

print(john.name, john.age, john.marks, john.grade)

dave = Student("Dave", 20, 356)
dave.calculate_grade()

print(dave.name, dave.age, dave.marks, dave.grade)
