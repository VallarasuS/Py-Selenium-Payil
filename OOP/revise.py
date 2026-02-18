class Student:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello", self.name)


student_1 = Student("John")
student_1.introduce()

student_2 = Student("Dave")
student_2.introduce()


class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        print("Size of Shape")


class Rectangle(Shape):

    # Method Override
    def area(self):
        print("Size of Rectangle")


s = Shape("Shape")
s.area()

rect = Rectangle("Rectangle")
print(rect.name)
rect.area()


from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def copy(self):
        pass


class FileStorage(Storage):

    def save(self):
        print("Saved")


class NetworkStorage(Storage):
    pass


file = FileStorage()
nw = NetworkStorage()

# Interview Prep

# - OOPS
# Inheritance
# Method overload
# Method override
# Abstraction
# Encapsulation
