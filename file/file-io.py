# FILE MODES

# - READ (B) - > r
# - WRITE (B) -> w
# - APPEND (B) -> a

# Read
# - Read (entire file)
# - ReadLine (line by line)
# - Read All Lines (Entire file as line)

# open -> path, mode

file = open(r"C:\Users\Valla\Desktop\temp\student-scores.csv", "r")
contents = file.read()
file.close()

print(contents)
