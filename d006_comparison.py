# student_score = 99
# student_two_score = 100
# centum = 100

# is_centum = student_two_score == centum
# print("Is Centum: ", is_centum)

# print("True Division:", 10 / 3)
# print("Floor Division", 10 // 3)

# number = 14

# remainder = number % 2
# print("Remainder: ", remainder)

# is_even = remainder == 0
# print("Is Even: ", is_even)

# signal = "green"  # red, yellow, green

# go = "green"

# stop = signal != go
# print("Signal", signal, "- Should Stop", stop)

# ------------------------

# and, or, not

# allow entry: id-card, temporary id card
# deny entry: no id-card, no temporary id card

has_id_card = False
has_temporary_id_card = True

allow_entry = has_id_card or has_temporary_id_card
print("Allow Entry:", allow_entry)

deny_entry = not has_id_card or not has_temporary_id_card
print("Deny Entry ?", deny_entry)

max_age = 5
max_height = 150

child_height = 140
child_age = 4

half_ticket = child_age < max_age or child_height <= max_height
print("half_ticket: ", half_ticket)

# Comparison Op, Home Work
# 1. Given age check if user can vote. min age 18
# 2. Given age check if user can drive min age 18
# 3. Given mark check if user fail. pass mark 36
# 4. Given mark check if user scored centum (100)
# 5. Given body temperature check if user has fever (more than 100)
# 6. Given number check if it prime number
