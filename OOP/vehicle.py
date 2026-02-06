class Vehicle:

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def drive(self):
        print("drive")


class Car:

    def start():
        pass

    def stop():
        pass

    def drive():
        pass


class Bus(Vehicle):

    def park(self):
        print("Parked")


b1 = Bus()
b1.stop()
b1.drive()
b1.start()
b1.park()
