numbers = [1, 2, 3, 4, 5]

print(numbers)
print(type(numbers))

numbers = ["one", 2, "three", True, False, 43.12]
print(numbers)
print(numbers[0])

# slicing -> Copy
print(numbers[0:2:1])
x = numbers[4 : len(numbers) : 1]

print(x)  # [False, 43.12]
x[0] = "False"  # modify - mutate
print(numbers)
print(x)

print("---")

for i in numbers:
    print(i)


numbers = [1, 2, 3, 4, 5]
print(numbers)

# Mutable
numbers[0] = 20
numbers[4] = 10

x = numbers[0]
y = numbers[4]

print(numbers)


# take one value at a time
numbers = [1, 2, "5", 4, "5"]
for i in numbers:
    i = int(i)
    print(i)


numbers = [1, 2, 5, 4, 5]
size = len(numbers)

for i in range(0, size, 1):
    x = numbers[i]
    print(x)

numbers = [1, 2, "Three", [3, 5, 6]]

x = numbers[3]
y = x[2]

print(numbers[3][2])

scores_data = [["John", 30, 40, 50], ["Dave", 50, 60, 70], ["Mike", 20, 30, 40]]


message = "Hello World"
list_char = list(message)
print(list_char)
