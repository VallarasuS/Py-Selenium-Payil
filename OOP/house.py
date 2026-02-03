class House:

    def __init__(self, number, paint):
        self.door_number = number
        self.paint = paint


house_one = House(100, "White")
house_two = House(120, "Grey")

print(type(house_one))
print(house_one.door_number)
print(house_one.paint)

print(house_two.door_number)
print(house_two.paint)


# def add(x, y):
#     return x + y


# add(10, 20)
