stream = [1, 2, 3, 4]

bucket = 0
for i in stream:
    bucket = bucket * i
    print("i = ", i)
    print(bucket)

print(bucket)

##########################################

numbers = [10, 20, 5, 5]

total = 0

for i in numbers:
    total = total + i

print(total)

######################################
# op -> 2, 4, 6
numbers = [1, 2, 3, 4, 5, 6]
even = []
for i in numbers:
    if i % 2 == 0:
        even.insert(0, i)

print(even)
