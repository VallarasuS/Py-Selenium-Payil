# Complete the following function(s)
# Given an year, return True if it is a leap year, False otherwise


def is_leap_year(year):
    pass


# ----------------------------------------------#
#      Do not modify the test code below        #
# ----------------------------------------------#


def validate(expected, actual):
    assert actual == expected, "Leap Year -> expected {0} got {1}".format(
        expected, actual
    )


result = is_leap_year(2016)
validate(expected=True, actual=result)

result = is_leap_year(2020)
validate(expected=True, actual=result)

result = is_leap_year(2026)
validate(expected=False, actual=result)
