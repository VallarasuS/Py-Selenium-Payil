class Student:

    def __init__(self, name, section, year, marks):
        self.name = name
        self.section = section
        self.year = year
        self.marks = marks

    def total(self):
        return sum(self.marks)


student_one = Student("John", "10 A", 2026, [30, 24, 24])
student_tw = Student("Dave", "12 B", 2026, [93, 59, 23])
mythili = Student("Mythili", "12 B", 2026, [32, 65, 85])

print(mythili.name, mythili.section, mythili.year)

print(mythili.total())
