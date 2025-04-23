class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other,point):
            return point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self,other):
        if isinstance(other,point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"({self.x}, {self.y})"


# Test cases
p1 = point(3, 4)
p2 = point(1, 2)

# Addition of points
p3 = p1 + p2  # Point(4, 6)

# Equality check
print(p1 == p2)  # False

# String representation
print(p1)  # (3, 4)
print(p3)  # (4, 6)