# Combined Program: Inheritance + Composition

# Base class (Inheritance)
class Animal:
    def eat(self):
        print(f"{self.__class__.__name__} is eating.")

# Additional capability class (Composition)
class Flyable:
    def fly(self):
        print(f"{self.__class__.__name__} is flying.")

# Specific Animals

class Lion(Animal):  # Inherits from Animal
    def roar(self):
        print("Lion roars!")

class Penguin(Animal):  # Inherits from Animal
    def swim(self):
        print("Penguin swims!")

class Bird(Animal):  # Inherits from Animal and uses Composition
    def __init__(self):
        self.flyable = Flyable()  # Composition: has-a Flyable

    def fly(self):
        self.flyable.fly()

# Testing the combined program
def main():
    print("Lion Actions:")
    lion = Lion()
    lion.eat()
    lion.roar()
    print()

    print("Penguin Actions:")
    penguin = Penguin()
    penguin.eat()
    penguin.swim()
    print()

    print("Bird Actions:")
    bird = Bird()
    bird.eat()
    bird.fly()

if __name__ == "__main__":
    main()
