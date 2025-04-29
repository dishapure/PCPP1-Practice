# "is-a" relationship: Car is a Vehicle
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):  # Car IS-A Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

# "has-a" relationship: Car has an Engine
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

class CarWithEngine(Car):  # Car HAS-A Engine
    def __init__(self, brand, model, engine_type):
        super().__init__(brand, model)
        self.engine = Engine(engine_type)  # Car has an engine

    def car_details(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Engine Type: {self.engine.engine_type}")

# Create objects
car = CarWithEngine("Toyota", "Corolla", "V6")
car.car_details()
