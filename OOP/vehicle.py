class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__isRunning = False

    def detail(self):
        print(self.make, self.model, self.year)

    def start(self):
        self.__isRunning = True
        print(self.make, "Started")

    def stop(self):
        self.__isRunning = False
        print("Stopped")

    def isRunning(self):
        if self.__isRunning:
            print(self.make, "Running")
        else:
            print(self.make, "Not Running")


ford = Vehicle("Ford", "Figo", "2020")
ford.detail()
ford.start()
ford.isRunning()

swift = Vehicle("Maruti", "Swift", "2022")
swift.detail()
swift.isRunning()
