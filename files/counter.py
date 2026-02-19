def read_count():
    file = open(r"C:\Users\Valla\Desktop\files\count.txt", "r")
    count = int(file.read())
    file.close()

    return count


def write_count(number):
    file = open(r"C:\Users\Valla\Desktop\files\count.txt", "w")
    file.write(str(number))
    file.close()


def counter(number):

    offset = read_count()  # 0

    for i in range(0, number, 1):  # 0, 10, 1
        number = i + 1 + offset  # 0, 1, 2, 3, 4, ... 9 + 1 + 0
        print(number)

    write_count(number)


counter(10)

# file = open(r"C:\Users\Valla\Desktop\files\count.txt", "w")
