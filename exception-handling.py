# x = 10
# y = 0
# z = x / y

# print(z)

# try, expect

# a = input("Enter a number: ")
# a = int(a) + 1
# print(a)

# try:
#     a = input("Enter a number: ")
#     a = a + 1
#     print(a)
# except TypeError:
#     print("Error Try again")

# x = input("Enter a number: ")
# y = input("Enter another number: ")
# z = int(x) / int(y)
# print(z)

try:
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    z = int(x) / int(y)
    print(z)
except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Invalid Input")
finally:
    print("End of try")
