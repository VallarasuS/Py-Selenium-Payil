# ------------------------ #
# STRING
# ------------------------ #
# - upper
# - lower
# - title
# - split
# - join
# - find
# - startswith
# - endswith
# - For more here - https://docs.python.org/3/library/stdtypes.html#textseq
# ------------------------ #

message = "Hello World"
print(message)

new_message = message.upper()
print(new_message)

new_message = message.lower()
print(new_message)

new_message = new_message.title()
print(new_message)

new_message = message.split()
print(new_message)

data = "John,30,IT,34958"  # CSV
print(data)
tokens = data.split(",")
print(tokens)

sep = "-"
sentence = sep.join(tokens)
print(sentence)


message = "scala, F# pattern matching, deconstruction"
index = message.find("pattern")
print(index)

starts_with = message.startswith("Scala")
print(starts_with)

ends_with = message.endswith("deconstruction")
print(ends_with)

op = "   Hello        World    "
op = op.strip()

# op = op.lstrip("x")
# op = op.lower().strip("x")
print(op)


# scala, F# pattern matching, deconstruction
# unpacking
# name, age = "john", 30

# name, age, dept, code = tokens  # ["John","30","IT","34958"]
# print(name)
# print(code)

# Truthy Values

x = "Hello World"
x = ""
x = None
x = 0
x = 100
x = 10

if x:  # -> True / False
    print("True")
else:
    print("False")
