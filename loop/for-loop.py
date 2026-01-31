# for i in range(1, 11, 1):
#     print(i)

# for i in range(2, 21, 2):
#     print(i)

# for i in range(5, 51, 5):
#     print(i)

# sum of first n numbers:

# 1, 2, 3, 4 -> (+) -> 10

# n = 5
# sum = 0

# for i in range(1, n, 1):
#     sum = sum + i

# print(sum)


# factor = 2

# for i in range(1, 11, 1):
#     print(i * 2)

# message = "Hello World"
# size = len(message) - 1

# char = ""

# for i in range(size, -1, -1):
#     char = char + message[i]

# print(char)


message = "Hello World"
size = len(message)  # -> 11
char = ""

for i in range(0, size, 1):
    # print(i)
    c = message[i]
    char = c + char

print(char)

# table 1-10 * n
# sum of n numbers -> 1,2,3,4 -> 10
# find position of a char in string
# Hello World -> 6
