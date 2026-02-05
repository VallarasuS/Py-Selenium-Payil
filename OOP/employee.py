class Employee:

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def increment(self, amount):
        self.salary = self.salary + amount


one = Employee("John", "EMP001", 15000)
print(one.name, one.id, one.salary)
one.increment(1000)
print(one.name, one.id, one.salary)

two = Employee("Dave", "EMP002", 16000)
print(two.name, two.id, two.salary)
two.increment(4000)
print(two.name, two.id, two.salary)


class Student:

    def __init__(self, name, ta, en, ma, sc, ss):
        self.name = name
        self.ta = ta
        self.en = en
        self.ma = ma
        self.sc = sc
        self.ss = ss

    def total(self):
        print("Total", self.ta + self.en + self.ma + self.sc + self.ss)
        return self.ta + self.en + self.ma + self.sc + self.ss

    def average(self):
        avg = self.total() / 5
        print("Average", avg)


arun = Student("Arun", 60, 45, 67, 34, 46)
vijay = Student("Vijay", 56, 76, 87, 99, 45)

arun.total()
arun.average()

vijay.total()
vijay.average()
