# ---------------------------------------
#               FILES
# ---------------------------------------

# mode: "w"
# - write: write a string
# - writelines: write list of lines

# write
# -------
# over writes
# creates if file does not exist

file = open(r"C:\Users\Valla\Desktop\py-file\file-write.txt", "w")
file.write("1. Hello World\n")
file.write("2. Hello World\n")
file.write("3. Hello World\n")
file.close()

# write lines
# --------------

with open(r"C:\Users\Valla\Desktop\py-file\file-write-lines.txt", "w") as f:
    lines = ["1. Hello World\n", "2. Hello World\n", "3. Hello World\n"]
    f.writelines(lines)

# ---------------------------------------

# mode: "a"
# appends to existing file
# - write: write a string
# - writelines: write list of lines

with open(r"C:\Users\Valla\Desktop\py-file\hello.txt", "a") as fh:
    lines = ["\n5. Hello World\n", "6. Hello World\n"]
    fh.writelines(lines)

# ---------------------------------------

# COPY
# ------------------
# Read from one dir
# Write to another dir

# Merge
# ------------------------
# Read from multiple files
# Write to single file
