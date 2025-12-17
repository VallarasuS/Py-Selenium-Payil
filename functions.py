def hello():
    print("Hello")
    print("Welcome to Python")


hello()


def add(x, y):
    print("X:", x)
    print("Y:", y)
    print("Sum X + Y :", x + y)


add(0, 1)
add(2, 1)
add(2, 3)


def mul(a, b):
    print("A :", a)
    print("B :", b)
    print("Mul A * B =", a * b)


mul(2, 3)


def login(user_name, password):
    print("Open Browser")
    print("Open URL")
    print("User Name:", user_name)
    print("Password: ", password)
    print("Login")

    username_valid = user_name == "John"
    password_valid = password == "1234"
    return username_valid and password_valid


login_result = login("John", "1234")
print("Login Result:", login_result)

print("-------")

login_result = login("John_", "1234")
print("Login Result:", login_result)

print("-------")

login_result = login("John", "1234_")
print("Login Result:", login_result)

login("John", "1234_")
login("John_", "1234_")

print("EOF")


def add(x, y):
    return x + y


result = add(2, 3)
print(result)

# Try yourself
# add,
# mul,
# sub,
# pow,
# div,
# floor_div

# print
# return
