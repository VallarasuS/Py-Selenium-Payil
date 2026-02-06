class Vehicle:

    def __init__(self, name):
        self.name = name

    def start(self):
        print("Started", self.name)

    def stop(self):
        print("Stopped", self.name)

    def drive(self):
        print("Drive", self.name)


# v1 = Vehicle("Vehicle")
# v1.start()
# v1.stop()


class Car(Vehicle):

    def __init__(self, name):
        super().__init__(name)


c1 = Car("TATA NANO")
c1.start()
c1.stop()
c1.drive()
