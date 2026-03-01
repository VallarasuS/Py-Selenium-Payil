# Data types
# int
# str
# bool
# float

import math

age = 30
name = "John Smith"

print(age)
print(name.upper())
print(name.lower())
print(name.startswith("Smith"))
print(name.endswith("Smith"))
print(name.split())
print(name.find("Smi"))

# Arithmetic Operators

add = 10 + 3
sub = 10 - 3
prod = 10 * 3
exp = 10**3

floor = 10 // 3
print(floor)

truediv = 10 / 3
print(truediv)
print(round(truediv, 2))

mod = 10 % 3
print(mod)

# PEMDAS () ** * / + -

# Comparison Operators

age = 12
can_vote = age >= 18

# >, >=, <, <=, ==, !=

# Logical Operators
# and or not

holds_voter_id = True
can_vote = age >= 18 and holds_voter_id

# Zero Trust
# Branching Statements

result = ""

if can_vote:
    result = "Can vote"
elif age == 18:
    result = "Can vote"
else:
    result = "User Can Not Vote"

print(result)

# Loop
# while -> driven by condition
# for   -> no of steps/iteration ahead

i = 0

while i < 10:
    print(i)
    i = i + 1

# stop, stop, step
for i in range(0, 10, 1):
    print(i)

numbers_list = [1, 2, 3, 4]

print(numbers_list[0])
numbers_list[0] = 10

for i in numbers_list:
    print(i)

for i in range(0, len(numbers_list), 1):
    print(numbers_list[i])

# # add
# append
# insert
# extend

# # delete
# pop
# clear

# # re-order
# sort
# reverse

params = ("john", 30, "Chennai")
# params[0] = "John S" - immutable

*rest, city = params
print(city)
print(rest)

colors = {"Red", "Green", "Blue", "Blue"}
print(colors)

# union, intersection, difference, symmetric difference

john = {"age": 30, "name": "john"}
# key - value pairs
# get, update


# default params
def add(x, y=1):
    print(x + y)


x = add(10, 2)
print(x)


def sub(x, y):
    return x - y


add(10, 20)
x = sub(20, 10)
print(x)

res = sub(x=10, y=5)
print(res)


# variable length parameter
def addition(*args):
    total = 0
    for i in args:
        total = total + i
    print(total)


addition(10, 20)
addition(10, 20, 30)
addition(10, 20, 30, 40)


numbers = [1, 2, 3, 4, 5, 6]

# membership
if 5 in numbers:
    print("numbers contain 4")
else:
    print("not in numbers")

# slicing, start:stop:step
print(numbers[1::2])
