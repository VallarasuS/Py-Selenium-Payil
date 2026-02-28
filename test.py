# name = "John Smith"
# print(name)

# # Ctrl + / - comment ignored by python compiler, interpreter

# age = 19 + 1  # Arithmetic 'add'
# height = 5.1

# print("Age :", age)
# print("Height :", height)

# can_vote = age > 18  # True
# print("Voting :", can_vote)

# numbers = [1, 2, 3, 4, 5]

# x = [i * i for i in numbers if i % 2 == 0]

# print(x)

# x = 2
# if x == 2:
#     y = "even"
# print(y)


x = 2
y = 3


def add(x, y):
    return x + y


x = add(10, 20)
print(x)


try:
    x = int(input("enter number"))
    y = int(input("enter another number"))
    z = x / y
except ZeroDivisionError:
    print("Cant divide by zero")
except ValueError:
    print("Invalid Input ")
except Exception:
    print("Error happened try again, restart")
finally:
    print("Clean up resource")
