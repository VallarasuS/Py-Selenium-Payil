# Tuple
# immutable, can not modify
# faster and low memory usage
numbers = (1, 2, 3, 4)
print(numbers)
print(type(numbers))

print("----")

# numbers[3] = 10
# print(numbers)

print(numbers[3])
print(sum(numbers))
print(max(numbers))
print(min(numbers))

print("---")

for i in numbers:
    print(i)

name = "John"
age = 30
year = 2025

# packing
employee = (name, age, year)
print(employee)

# unpacking
x, y, z = employee
print(x)
print(y)
print(z)

ta = 50
en = 40
ma = 60

scores = (ta, en, ma)

total = sum(scores)
top = max(scores)

avg = total / len(scores)
print(avg)
