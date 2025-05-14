class Car:
    def start_engine(self):
        print("Car engine started!")

    def move(self):
        print("Car is driving!")

class Boat:
    def start_engine(self):
        print("Boat engine started!")

    def move(self):
        print("Boat is sailing!")

class Bicycle:
    def move(self):
        print("Bicycle is  moving forward!")

vehicals = [Car(),Boat(),Bicycle()]
for vehicle in vehicals:
    try:
        vehicle.start_engine()
    except AttributeError:
        print("This vehicle has no engine!")
    vehicle.move()
