numbers = (1, 2, 3, 2, 1)
print(numbers)

data = ("John", 30, 54.5, "Engineer")
print(data)

# immutable
# print(data[0])
# data[0] = "Dave"

# unpack
name, age, weight, qualification = data
age = age + 1
# packing
data = (name, age, weight, qualification)
print(data)


def increment(e, value):
    name, department, salary = e  # un-packing
    salary = salary + value
    return (name, department, salary)  # packing


employee = ("John", "IT", 25000)
print(employee)

new_employee = increment(employee, 1000)
print(new_employee)
