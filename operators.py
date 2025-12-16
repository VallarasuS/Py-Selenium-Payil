x = 100
y = 150
z = x + y

print(z)
print(2**3)
print(10 % 3)

revenue = 20000
salary = 8000
head_count = 2

net_payable = head_count * salary
print(net_payable)

profit = revenue - net_payable
print(profit)

profit = revenue % salary
print(profit)

age = 20
min_age = 18
can_vote = age > min_age

print(can_vote)

# == -> comparison operator
# = -> Assignment Operator

# = -> x = 10
# x -> variable
# 10 -> value
# = -> Assignment operator

# 1. Given age check if user can vote. min age 18
# 2. Given age check if user can drive min age 18

age = 16
min_age_vote = 18  # 18 or above can vote

can_vote = age >= min_age_vote
print("Can Vote? :", can_vote)

print(type(can_vote))

has_license = True
min_age_drive = 18
age = 19


can_drive = age >= min_age_drive and has_license
print("Can Drive :", can_drive)

has_id_card = True
has_temporary_card = False

can_enter = has_id_card or has_temporary_card

print("Can Enter? :", can_enter)

can_not_enter = not has_id_card and not has_temporary_card
print("Deny Entry:", can_not_enter)

age_limit = 5
max_height = 155

age = 4
height = 130

half_ticket = not age > age_limit

print("Half Ticket :", half_ticket)

door_closed = False
can_deliver = not door_closed
print("Can Deliver?: ", can_deliver)

# 6. Given number check if it is odd
# 7. Given number check if it is even

number = 100
is_even = (number % 2) == 0
print("Is even? :", is_even)

remainder = number % 2
print("Remainder = ", remainder)

is_odd = number % 2 != 0
print("IS Odd? ", is_odd)
