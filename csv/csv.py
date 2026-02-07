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


# process input string
# - split into lines
# - skip first line
# - split lines into works
# - process only numbers, skip strings
# calculate sum, average, top
# add it back to the line
# combine all lines

# DRY - Do not repeat yourself
# Single Responsibility - do one job, do it well
data = "Name, City, Math, Science, Language \n John, Chennai, 40, 60, 50 \n Dave, Chennai, 34, 60, 50 \n Steve, Bangalore, 34, 60, 50"

from parse import split
from calc import stats

lines = split(data, "\n", 1)
for line in lines:  # John, Chennai, 40, 60, 50
    words = split(line, ",", 2)  # ["John", "Chennai", "40", "60", "50"]
    total, average, topScore = stats(words)  # 150, 50, 60
    result = f"{line},{total},{average},{topScore}"
