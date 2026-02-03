class Student:

    # initializes Student object
    # called by python
    # self, name -> parameters -> python provides self
    # name -> provided by developer
    def __init__(self, name):
        self.name = name


student_one = Student("John")
# student_one.name = "John"

student_two = Student("Dave")
# student_two.name = "Dave"

print(student_one.name)
print(student_two.name)
