# prints to terminal
# return type -> None -> Nothing to return
print("Hello World")

# reads input from terminal
# return type string
name = input("Enter your name: ")
print(name)

# PEMDAS
x = 10 + 20 - 5 * 2
print(x)

centum = 100
score = 90
is_centum = score == centum

age = 16
voting_age = 18
can_vote = age >= voting_age

print(can_vote)


def div(x, y):
    return x / y


def floor_div(x, y):
    return x // y


print(div(10, 2))

print(floor_div(10, 2))


def max(x, y):
    if x > y:
        return x
    else:
        return y


print(max(10, 20))
