# ---------------------------------------
#               FILES
# ---------------------------------------


# Modes
# ---------------------------------------
# - Read
# -------------

#   - read-only
#   - "r"
#   - if file doesn't exist - throws error

# - Write
# -------------

#   - read and write
#   - "w"
#   - if file doesn't exist - creates file
#   - write - over writes file, all old contents are lost

# - Append
# -------------

#   - read and write
#   - "a"
#   - if file doesn't exist - creates file
#   - write adds to existing file contents

# open("path", mode) -> file handle
#   - read: reads all file content at string
#   - readline: read one line at a time
#   - readlines: reads all content as list of lines

# ---------------------------------------

file = open(r"C:\Users\Valla\Desktop\py-file\hello.txt", "r")

content = file.readline()
print(content)

file.close()

message = 'Hello "John"'
print(message)

# ---------------------------------------

file = open(r"C:\Users\Valla\Desktop\py-file\hello.txt", "r")

content = file.readline()
print(content)

while len(content) > 0:
    content = file.readline()
    print(content)

file.close()

# ---------------------------------------

try:
    file = open(r"C:\Users\Valla\Desktop\py-file\hello.txt", "r")

    content = file.readlines()
    print(type(content))
    print(content)

    file.write("Hello")  # throws error, cant write in read-mode
    file.close()

except FileNotFoundError:
    print("File does not exist! Try again!")

with open(r"C:\Users\Valla\Desktop\py-file\hello.txt", "r") as file:
    content = file.readlines()
    print(type(content))
    print(content)

# ---------------------------------------
