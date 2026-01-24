# "John,30,2026" -> "John,31,2027"


def csv_incr_year_and_age(input_data):

    tokens = input_data.split(",")  # ["John", "30", "2026"]
    name, age, year = tokens
    age = int(age) + 1
    year = int(year) + 1

    res = ",".join([name, str(age), str(year)])
    res = f"{name},{age},{year}"
    print(res)

    return res


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, f"Search -> expected {expected} got {actual}"


result = csv_incr_year_and_age("John,20,2026")
validate(expected="John,21,2027", actual=result)

result = csv_incr_year_and_age("Sam,12,2018")
validate(expected="Sam,13,2019", actual=result)

result = csv_incr_year_and_age("Dave,32,1950")
validate(expected="Dave,33,1951", actual=result)
