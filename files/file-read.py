# file handling

# MODES
# r -> read
# w -> write
# a -> append

# function - open(path, mode) -> opens file
# function - close() -> closes the file

# Read - Read All Lines as a string
# ---------------------------------

file = open(r"C:\Users\Valla\Desktop\temp\quotes.txt", "r")
contents = file.read()
print(contents)
file.close()

# Read Line - Read one line at a time
# ---------------------------------

quotes = open(r"C:\Users\Valla\Desktop\temp\quotes.txt", "r")

line = quotes.readline()
print(line)

line = quotes.readline()
print(line)

quotes.close()

# Read Lines - Read all lines as a list
# ---------------------------------

fq = open(r"C:\Users\Valla\Desktop\temp\quotes.txt", "r")
list_quotes = fq.readlines()
print(list_quotes)
fq.close()

print(type(list_quotes))
print(len(list_quotes))
