from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Cat(Animal):

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "Meow")


cat_one = Cat("Meow")
cat_one.speak()


class Cow:

    def speak(self):
        print("Moo")


cow_one = Cow()
cow_one.speak()
