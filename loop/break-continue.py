def find(source, key):
    position = -1
    for i in range(0, len(source), 1):

        if key == source[i]:
            position = i
            break

    return position


pos = find("Hello World Really long string", "W")
# print(pos)


def even_numbers(n):

    if n < 0:
        return "Invalid Input"

    for i in range(1, n, 1):

        if i % 2 != 0:
            continue

        print(i)

        # if i % 2 == 0:
        #     print(i)


even_numbers(20)
