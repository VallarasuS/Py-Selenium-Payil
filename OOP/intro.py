# blue print
class Student:

    # double under, dunder function to
    # create, initialize, construct
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def hello(self):
        print("Hello my name is", self.fname)


# creation, construct, initialization
john = Student("John", "Smith")
adam = Student("Adam", "Jones")

# type check: one is object of Student class
print(type(john))
# print(john.fname)
# print(adam.fname)
john.hello()
adam.hello()


class Student:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def hello(self):
        print("Hello my name is", self.fname)


john = Student("John", "Smith")
adam = Student("Adam", "Jones")

john.hello()
adam.hello()
