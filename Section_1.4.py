# Base class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

    def describe(self):
        print(f"This is a {self.species} named {self.name}.")

# Subclass of Animal
class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.is_warm_blooded = True

    def make_sound(self):
        print("Mammal sound")

    def describe(self):
        print(f"{self.name} is a warm-blooded {self.species}.")

# Subclass of Animal
class Bird(Animal):
    def __init__(self, name, species, can_fly):
        super().__init__(name, species)
        self.can_fly = can_fly

    def make_sound(self):
        print("Chirp chirp")

    def describe(self):
        flight_status = "can fly" if self.can_fly else "cannot fly"
        print(f"{self.name} is a bird that {flight_status}.")

# Subclass of Mammal
class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def make_sound(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} is fetching!")

    def describe(self):
        print(f"{self.name} is a loyal dog.")

# Subclass of Bird
class Parrot(Bird):
    def __init__(self, name):
        super().__init__(name, "Parrot", can_fly=True)

    def make_sound(self):
        print("Squawk!")

    def repeat_words(self, words):
        print(f"Parrot says: {words}")

    def describe(self):
        print(f"{self.name} is a colorful parrot that can mimic sounds.")

# Testing the classes
animal = Animal("Generic", "Unknown")
mammal = Mammal("Leo", "Lion")
bird = Bird("Pengu", "Penguin", can_fly=False)
dog = Dog("Buddy")
parrot = Parrot("Polly")

# Calling all methods
print("\n--- Individual Descriptions and Sounds ---")
animal.describe()
animal.make_sound()

mammal.describe()
mammal.make_sound()

bird.describe()
bird.make_sound()

dog.describe()
dog.make_sound()
dog.fetch()

parrot.describe()
parrot.make_sound()
parrot.repeat_words("Hello!")

# Polymorphism: loop through all and call make_sound()
print("\n--- Polymorphism Example ---")
animals = [animal, mammal, bird, dog, parrot]
for a in animals:
    print(f"{a.name} says:", end=" ")
    a.make_sound()


