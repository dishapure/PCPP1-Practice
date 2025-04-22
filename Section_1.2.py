import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # String representation for print()
    def __str__(self):
        return "Vector(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    # Debugging representation
    def __repr__(self):
        return "Vector3D(x=" + str(self.x) + ", y=" + str(self.y) + ", z=" + str(self.z) + ")"

    # Equality check
    def __eq__(self, other):
        if isinstance(other, Vector3D):
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        return False

    # Not equal check
    def __ne__(self, other):
        return not self.__eq__(other)

    # Absolute value (magnitude)
    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Type conversion to float
    def __float__(self):
        return abs(self)

    # Type conversion to int
    def __int__(self):
        return int(abs(self))

    # Attribute access
    def __getattr__(self, name):
        if name == "length":
            return abs(self)
        raise AttributeError("'Vector3D' object has no attribute '" + name + "'")

    # Container-like access
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index must be 0, 1, or 2")

    # Optional: Custom instance check
    def __instancecheck__(self, instance):
        return hasattr(instance, 'x') and hasattr(instance, 'y') and hasattr(instance, 'z')


# ✅ Sample usage
if __name__ == "__main__":
    v1 = Vector3D(3, 4, 0)
    v2 = Vector3D(3, 4, 0)
    v3 = Vector3D(0, 0, 5)

    print(v1 == v2)  # True
    print(v1 != v3)  # True
    print(abs(v1))  # 5.0
    print(float(v1))  # 5.0
    print(int(v3))  # 5
    print(v1.length)  # 5.0
    print(v3[2])  # 5
    print(str(v1))  # Vector(3, 4, 0)
    print(repr(v1))  # Vector3D(x=3, y=4, z=0)
    print(isinstance(v1, Vector3D))  # True
