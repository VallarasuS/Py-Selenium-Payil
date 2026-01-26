# x = 1
# total = 0
# while x <= 4:
#     total = total + x
#     x = x + 1

# print(total)


# print even numbers until 20

x = 1

# while x <= 20:
#     x = x + 1
#     if x % 2 == 0:
#         print(x)

# # x = 1

# while x <= 20:
#     x = x + 1
#     remainder = x % 2
#     if remainder != 0:
#         continue

#     # final out
#     print(x * 2)

n = 0

while n <= 100:
    n = n + 1
    if n % 3 == 0 and n % 5 == 0:
        print(n)
        break


print("Rest of the program")
