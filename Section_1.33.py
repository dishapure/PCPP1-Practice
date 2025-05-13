# -*- coding: utf-8 -*-  # Default encoding declaration (optional in Python 3)

"""
PEP Demonstration Module

This script demonstrates PEP 1, PEP 8, PEP 20, and PEP 257.
Includes examples of docstrings, naming conventions, layout, and type hints.
"""

# -------------------------------
# ✅ MODULE IMPORTS (PEP 8 2.2)
# -------------------------------

import math  # Standard library import
import sys  # One import per line – don't group multiple imports


# Third-party imports would go next
# Local application imports would follow


# -------------------------------
# ✅ FUNCTION DEFINITIONS (PEP 257 + PEP 484)
# -------------------------------

def calculate_area(radius: float) -> float:
    """
    One-line docstring (PEP 257) using triple double-quotes.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: Area of the circle.
    """
    return math.pi * (radius ** 2)  # 4-space indentation (PEP 8)


def calculate_volume(radius: float, height: float) -> float:
    """
    Multi-line docstring with descriptions of parameters and return type.

    Args:
        radius (float): Radius of the base.
        height (float): Height of the cylinder.

    Returns:
        float: Volume of the cylinder.
    """
    return math.pi * (radius ** 2) * height


# -------------------------------
# ✅ CLASS DEFINITION (PEP 8 Naming + Docstring)
# -------------------------------

class Cylinder:
    """Class names use CapitalizedWords convention (PEP 8)."""

    def __init__(self, radius: float, height: float) -> None:
        """
        Constructor with docstring and type hints (PEP 484).

        Args:
            radius (float): Radius of the cylinder.
            height (float): Height of the cylinder.
        """
        self.radius = radius  # Instance variables use lowercase_with_underscores
        self.height = height

    def surface_area(self) -> float:
        """Returns surface area; method names are lowercase_with_underscores."""
        return (2 * math.pi * self.radius * self.height +
                2 * math.pi * (self.radius ** 2))  # Hanging indent (PEP 8)

    def volume(self) -> float:
        """Returns the volume of the cylinder."""
        return math.pi * (self.radius ** 2) * self.height


# -------------------------------
# ✅ STRING QUOTES, COMMENTS, NAMING
# -------------------------------

def print_cylinder_details(cylinder: Cylinder) -> None:
    """Prints the surface area and volume (PEP 257 docstring)."""
    print(f"Surface Area: {cylinder.surface_area()}")  # Double-quoted strings preferred
    print(f"Volume: {cylinder.volume()}")


# -------------------------------
# ✅ MAIN FUNCTION + WHITESPACE RULES
# -------------------------------

def main() -> None:
    """Main function to demonstrate execution."""

    # 🟡 No extra spaces before or after = in assignments (PEP 8)
    message = "Welcome to the Cylinder Calculator!"  # Double-quoted string
    print(message)

    # 🟢 Inline comments start with # and one space (PEP 8)
    radius = 3.0  # Radius in cm
    height = 5.0  # Height in cm

    # 🟢 Block comments for explaining a section of code
    # Create Cylinder object with radius and height
    my_cylinder = Cylinder(radius=radius, height=height)

    # Print the details (surface area and volume)
    print_cylinder_details(my_cylinder)


# -------------------------------
# ✅ ENTRY POINT (PEP 8 standard)
# -------------------------------

if __name__ == "__main__":
    main()

    # Importing PEP 20: "The Zen of Python"
    import this
