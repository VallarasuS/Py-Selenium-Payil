# x=20 > y=10 -> True - X is big
# x=10 > y=20 -> False - Y is big

x = 20
y = 10

# if x > y:
#     print(x)
# else:
#     print(y)


def max(x, y):
    # x > y -> x
    if x > y:
        return x
    else:
        return y


result = max(20, 10)
print(result)  # -> 20

result = max(10, 30)
print(result)  # -> 30

# max(10, 20) -> 20
# max(20, 10) -> 20

# 10 ? 20 ?
# Compare -> >,<,>=,<=, ==, !=

# x=20 > y=10 -> True - X is big
# x=10 > y=20 -> False - Y is big
