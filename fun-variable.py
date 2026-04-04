def add(*args):
    print(type(args))
    total = 0
    for i in args:
        total = total + i
    print(total)


add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)
add(10, 20, 30, 40, 50)