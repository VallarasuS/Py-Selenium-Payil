# modes
# r -> read
# w -> write

# write
file = open(r"C:\Users\Valla\Desktop\temp\hello.txt", "w")
file.write("Hello World \nWritten from python \n")
file.close()

# wite lines - multiple lines
file = open(r"C:\Users\Valla\Desktop\temp\multiline.txt", "w")
file.writelines(["Hello World \n", "Written from Python \n"])
file.close()
