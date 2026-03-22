class Student:

    def __init__(self, fname, lname, id):
        self.name = fname + " " + lname
        self.id = id


s1 = Student("John", "Smith", 100)
print(s1.name)

s3 = Student("Dave", "Jones", 102)
print(s3.name)
