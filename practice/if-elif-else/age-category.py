# Complete the following function(s)
# Given age categorize as follows
# "Child" (0–12)
# "Teen" (13–19)
# "Adult" (20–64)
# "Senior" (65+)


def categorize(age):
    pass


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, "Age -> expected {0} got {1}".format(expected, actual)


result = categorize(8)
validate(expected="Child", actual=result)

result = categorize(14)
validate(expected="Teen", actual=result)

result = categorize(32)
validate(expected="Adult", actual=result)

result = categorize(68)
validate(expected="Senior", actual=result)

result = categorize(-1)
validate(expected="Invalid", actual=result)
