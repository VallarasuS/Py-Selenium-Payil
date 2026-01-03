def div():
    x = 10
    y = 3
    z = x // y
    print("Div:", z)


div()


def add(x, y):
    z = x + y
    print("Sum of X, Y = ", z)


add(10, 20)


def mul(a, b):
    c = a * b
    print("Mult = ", c)


mul(5, 3)


def sum(a, b):
    c = a + b
    print("SUM >> ", c)
    return c


a = 10
b = 20
c = sum(a, b)

print(a, b)
print("Value Returned :", c)

# Given age check if user can vote. min age 18
