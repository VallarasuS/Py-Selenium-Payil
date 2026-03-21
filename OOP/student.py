class Student:

    def __init__(self, fname, lname, id):
        self.name = fname + " " + lname
        self.id = id


s1 = Student("John", "Smith", "100")
print(s1.name)


# class HomePage:

#     def __init__(self, url):
#         self.url = url
