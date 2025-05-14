# Problem 2

class X:
    def display(self):
        print("X's display method")

class Y(X):
    def display(self):
        print("Y's display method")

class Z(Y):
    def display(self):
        print("Z's display method")

class P(Y, X):
    pass

# Creating objects
z_obj = Z()
z_obj.display()  # Calls Z's display()

p_obj = P()
p_obj.display()  # Calls Y's display() because P inherits Y first

# Printing MRO
print(Z.__mro__)
print(P.__mro__)
