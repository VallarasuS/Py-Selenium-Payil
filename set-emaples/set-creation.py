# LIST
# Collection of data
# numbers = [1, 2, 3, 4, 5, 5, 5]
# print(numbers)

# numbers = []


# SET
# Collection of unique data
# without duplicates

# nums = set(numbers)
# print(type(nums))
# print(nums)

# print(dir(nums))

# all_days = {
#     "sunday",
#     "monday",
#     "tuesday",
#     "wednesday",
#     "thursday",
#     "friday",
#     "saturday",
#     "sunday",
# }

# print(all_days)

## operations

# add
# remove
# pop
# clear
# discard

# x = all_days.pop()
# print(x)
# print(all_days)

# all_days.remove("friday")
# print(all_days)


# all_days.clear()
# print(all_days)

# review list examples

all_days = {
    "mon",
    "tue",
    "wed",
    "thu",
    "fri",
    "sat",
    "sun",
}

week_end = set()
week_end.add("sat")
week_end.add("sun")

print(week_end)

week_days = {"mon", "tue", "wed", "thu", "fri"}
print(week_days)

# union operator
union = week_days | week_end
print(union)

# intersection
intersection = week_days & all_days
print(intersection)

# difference
difference = all_days - week_days
print(difference)

movie_one_visitors = {"John", "Dave", "Mathew"}
movie_two_visitors = {"James", "Derik", "Mathew"}
symmetric_difference = movie_one_visitors ^ movie_two_visitors

print(symmetric_difference)
