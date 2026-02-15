# numbers = (3, 4, 5, 1, 2)

# print(len(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(min(numbers))

# print(numbers)
# print(type(numbers))

# nums = [1, "three", 5, "seven", 9, 1, 1]
# tup_nums = tuple(nums)

# print(tup_nums)
# print(type(tup_nums))

# i = tup_nums.index("three")
# c = tup_nums.count(1)

# print(dir(tup_nums))


def stats(x, y, z):
    total = x + y + z
    avg = total / 3
    top = max([x, y, z])

    print(total, avg, top)  # unpacking


# un-packing
# tot, avg, top = stats(1, 2, 3)
# print(tot, avg, top)

john = ("John", 14, 45, 12, 34)
mike = "Mike", 12, 45, 76, 34

list_of_tuples = [john, mike, ("Dave", 12, 43, 95, 23)]

for record in list_of_tuples:

    # un-packing
    name, age, s1, s2, s3 = record
    print(name)
    stats(s1, s2, s3)


# john.sort()
