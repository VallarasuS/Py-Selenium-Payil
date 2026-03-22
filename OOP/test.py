class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def hello(self):
        print("Hello my name is", self.fname, self.lname)


p1 = Person("John", "Smith")
p2 = Person("Bryan", "Adams")

p1.hello()
p2.hello()
