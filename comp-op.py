x = 10
y = 5

is_x_greater = x > y

print(is_x_greater)

a = 20
b = 10

is_a_lesser = a < b
print(is_a_lesser)

age = 16
can_vote = age > 18

print(can_vote)

age = 12
can_drive = age > 18
print("Can Drive ?:", can_drive)

age = 20
is_minor = age < 18
print("Is Minor ", is_minor)

score = 35
pass_or_fail = score >= 35
print("Pass ?", pass_or_fail)

has_failed = score <= 34
print("failed ?", has_failed)

signal = "green"
can_go = signal == "green"

print("Can go?", can_go)

must_stop = signal != "green"
print("Stop?", must_stop)

age = 21
has_license = False
can_drive = age > 18 and has_license

print("Can Drive", can_drive)

age = 3
height = 160

half_ticket = age < 5 or height < 150
print("Half Ticket:", half_ticket)

temp = 102
has_fever = temp >= 100

print("fever", has_fever)

can_vaccinate = not has_fever
print("Vaccinate", can_vaccinate)

language_score = 50


def is_qualified(score):
    return score < 34


qualified = is_qualified(language_score)

print("Qualified ?", qualified)
