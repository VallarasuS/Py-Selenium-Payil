# Input
# Name, City, Math, Science, Language
# John, Chennai, 40, 60, 50
# Dave, Chennai, 34, 60, 50
# Steve, Bangalore, 34, 60, 50

# Expected Output
# Name, City, Math, Science, Language, Total, Average, Top Score
# John, Chennai, 40, 60, 50, 150, 50, 60
# Dave, Chennai, 34, 60, 50
# Steve, Bangalore, 34, 60, 50

from parse import split_into_lines, split_into_chars
from calc import add

data = "Name, City, Math, Science, Language \n John, Chennai, 40, 60, 50 \n Dave, Chennai, 34, 60, 50 \n Steve, Bangalore, 34, 60, 50"

# process input string
# - split into lines
# - skip first line
# - split lines into works
# - process only numbers, skip strings
# calculate sum, average, top
# add it back to the line
# combine all lines

lines = split_into_lines(data)
print(lines)

for line in lines:
    chars = split_into_chars(line, 2)

    total = add(chars)
    print(total)

    result = f"{line},{total}"
    print(result)
