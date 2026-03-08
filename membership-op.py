def is_valid_phone(phone):
    for ch in phone:
        if (
            ch.isdigit()
            or ch == " "
            or ch == "+"
            or ch == "-"
            or ch == "("
            or ch == ")"
        ):
            continue
        else:
            return False

    return True


def validate(phone):
    for ch in phone:
        # membership operator
        if ch in "+-,() 0123456789":
            continue
        else:
            return False
    return True


def validate(phone):
    for ch in phone:
        # membership operator
        if ch not in "+-,() 0123456789":
            return False

    return True


print(validate("(080) 2364 5654"))
print(validate("(+080)$ 123 5654"))

# print format
name = "John"
phone = "789 356 125"
email = "john@gmail.com"
print(f"{name:<10} | {phone:>14} | {email:<50}")


# append, insert, extend
# pop, remove, clear
# sort, reverse

# upper, lower, title
# split, join
# strip, lstrip, rstrip
# startswith, endswith
# find
# isdigit, isalpha,

print(dir(str))
