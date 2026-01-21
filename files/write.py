# r -> read
# w -> write (over write)
# a -> append (add to existing content)

# pen
qty = 100
price = 10
sold = 0
revenue = 0


# create file if not exists already
# file.write("Hello World")

# string join
# concatenation
# format
# a + b


def read():
    global qty, sold, revenue, price

    file = open(r"C:\Users\Valla\Desktop\temp\pen.log", mode="r")
    data = file.readline()

    delimiter = ","
    tokens = data.split(delimiter)

    qty = int(tokens[0])
    sold = int(tokens[1])
    price = int(tokens[2])
    revenue = int(tokens[3])


def save(qty, price, sold, revenue):
    file = open(r"C:\Users\Valla\Desktop\temp\pen.log", mode="w")
    delimiter = ","
    pen_inventory = delimiter.join((str(qty), str(price), str(sold), str(revenue)))
    print(pen_inventory)
    file.write(pen_inventory)
    file.close()


def sell(units):
    global qty, sold, revenue, price

    qty = qty - units
    sold = sold + units
    revenue = revenue + (units * price)


read()

sell(10)
sell(10)

# pen_inventory = str(qty) + "," + str(price) + "," + str(sold) + "," + str(revenue)
# pen_inventory = "{0},{1},{2},{3}".format(qty, price, sold, revenue)


save(qty, price, sold, revenue)
