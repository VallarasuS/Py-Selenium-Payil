# message = "This is python"

# file = open(r"C:\Users\Valla\Desktop\files\write-ex.txt", "w")
# file.write(message)

# file.close()


# lines = ["Hello \n", "This is written form python"]

# file = open(r"C:\Users\Valla\Desktop\files\write-lines-ex.txt", "w")
# file.writelines(lines)

# file.close()

lines = ["Hello \n", "This is written form python"]
file = open(r"C:\Users\Valla\Desktop\files\write-ap.txt", "a")
file.writelines(lines)
file.close()
