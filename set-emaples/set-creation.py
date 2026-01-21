numbers_set = {1, 2, 3, 4, 4, 4, 5, 5}

print(numbers_set)
print(type(numbers_set))

# print(dir(set))

# add
# remove
# clear
# pop
# operators

numbers_set.add(6)
numbers_set.add(1)
numbers_set.remove(4)
# numbers_set.clear()
numbers_set.pop()
print(numbers_set)

fruits = {"apple", "orange", "pineapple", "papaya", "orange"}
fruits.add("apple")
print(fruits)

primary_colors = {"Red", "Green", "Blue"}


week_days = {"Mon", "Tue", "Wed", "Thu", "Fri"}
week_end = {"Sat", "Sun"}

all_days = week_days | week_end
print(all_days)

work_days = all_days - week_end
print(work_days)

week_off = all_days - week_days
print(week_off)

# traveling

john = {"cloths", "food", "snack", "drinks", "laptop", "iphone", "charger", "money"}
dave = {"cloths", "food", "snack", "drinks", "iphone", "charger", "money"}

common = john & dave
print(common)

# snack
# charger
# drinks,
# food

symmetric_difference = john ^ dave
print(symmetric_difference)
