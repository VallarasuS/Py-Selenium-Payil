# run into error

# try, except, finally

try:
    # file open
    x = int(input("enter num: "))
    y = int(input("another num: "))
    print(x + y)
except ValueError:
    print("Invalid value, enter numbers")
except ZeroDivisionError:
    print("Can not divide by zero:")
except Exception as e:
    print("Error:", e)
finally:
    # file close
    print("from finally block")
