class Vehicle:

    def drive(self):
        print("Runs on petrol")


class EVehicle(Vehicle):

    def drive(self):
        print("Runs on battery")


# create an object of EVehicle
ev = EVehicle()
# method overriding
ev.drive()


vehicle = Vehicle()
vehicle.drive()
