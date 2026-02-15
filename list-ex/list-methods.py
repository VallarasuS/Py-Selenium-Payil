# # # ADD
# # # - append - add to end of list (Last In)
# # # - insert - add at specific index
# # # - extend - merge / extend two list

# # # Delete
# # # - pop - removes the last element (First Out)
# # # - remove - removes a specific element
# # # - clear - clear entire list

# # # Re-ordering
# # # sort - asc, desc order
# # # reverse - reverses the order in which elements were added

# # numbers = [3, 5, 1, 4]
# # even = [2, 4, 6]

# # # numbers.append(2)
# # # numbers.insert(10, 1)
# # # numbers.extend(even)

# # print(even)
# # print(numbers)

# # # print("Hello" + "World")
# # # print(numbers + even)

# # # print("Hi" * 3)
# # # print(even * 3)

# # # print(1 + 3)
# # # print(1 * 3)

# # # add - append, insert, extend
# # # delete - pop, remove, clear
# # sort, reverse
# # numbers = [5, 1, 3, 4]

# # x = numbers.pop()
# # numbers.remove(2)
# # numbers.clear()

# numbers = [5, 1, 3, 4]

# numbers.sort()  # -> 1, 3, 4, 5
# print(numbers)

# numbers.sort(reverse=True)  # -> 5, 4, 3, 1
# print(numbers)

# # Rotate the list N times - N = 2
# # [1, 2, 3, 4, 5] -> [5, 1, 2, 3, 4] -> [4, 5, 1, 2, 3]
# # total, squaring a list, find evens
# # reversing a list
# # sort a list -> asc, desc ->


# def add(x, y):
#     return x + y


# add(10, 20)
# add(x=10, y=20)


# nums = [4, 3, 1, 2]
# x = nums
# x.sort()
# print(nums)

# nums.sort(reverse=True)
# print(x)

# non - primitive

# object / class
# int, float, str, bool
nums = [4, 2, 6, 1, 5]
# Copy of sorted seq
x = sorted(nums)
print(nums)
print(x)
