# numbers = [5, 10, 15, 20, 25]
# total = sum(numbers)
# top = max(numbers)
# print(total)
# print(top)

# text = ["Hello", "world"]
# size = len(text)
# print(size)

# mixed = [1, "Hi", True, 3.14, text]


# for i in range(1, 11, 1):
#     print(i)

# print("---")

# numbers = [5, 10, 15, 20, 25]
# for i in numbers:
#     print(i)

# [] -> Create
# list() -> Create
# sum - total
# max - top value
# len - size of list
# loop - iterate over list

# print("----")

# marks = [35, 80, 75, 65, 90]
# total = 0

# for mark in marks:
#     total = total + mark

# print(total)

# # Index based access
# marks = [35, 80, 75, 65, 90]
# print(marks)

# # write
# marks[0] = 50

# # read
# print(marks[0])

# # read
# cut_off = marks[2] + (marks[3] / 2) + (marks[4] / 2)
# print(cut_off)

# print(dir(list))

# Add
# - Append - Add at the end
# - Insert - Add at an index

# Delete
# - Clear - deletes everything
# - Pop - deletes last element!
# - Remove - removes given element

# Add

fruits = ["apple", "custard apple", "orange", "banana"]
print(fruits)

fruits.append("grapes")
print(fruits)

fruits.insert(1, "mango")
print(fruits)

# ['apple', 'mango', 'orange', 'grapes']

# Delete

# x = fruits.pop()
# print(x)

# fruits.pop(1)
# print(fruits)

# fruits.remove("mango")
# print(fruits)

# fruits.clear()
# print(fruits)

# Ordering

# ['apple', 'mango', 'orange', 'grapes']

fruits.reverse()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits_copy = fruits.copy()
fruits_copy.pop()
print(fruits)
print(fruits_copy)
