# open (path, mode=r) - default read mode
# read
# read line
# read lines

# default mode - (r) -> read
file = open(r"C:\Users\Valla\Desktop\temp\quotes.txt")

# read entire file
# all_quotes = file.read()
# print(all_quotes)

# # read line by line, better memory
# # reads first line
# quote = file.readline()
# print(quote)

# # position set to next line
# # reads second line
# quote = file.readline()
# print(quote)

# reads and returns list of lines
# list_of_quotes = file.readlines()

# for q in list_of_quotes:
#     print(q, end="")
#     print("---")

quote = file.readline()

tokens = quote.split("-")
print(tokens[0].strip())
print(tokens[1].strip())


file.close()
