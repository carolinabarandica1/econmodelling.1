from colour_point import ColourPoint

class AdvancedPoint(ColourPoint):
    # Class-level variable containing allowed colours (uppercase by naming convention)
    COLOURS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, colour):
        """
        Initialises a new AdvancedPoint instance.
        Extends functionality from ColourPoint and Point.
        :param x: x-coordinate (int or float)
        :param y: y-coordinate (int or float)
        :param colour: string indicating the colour
        """
        if colour not in self.COLOURS:
            raise TypeError(f"Invalid colour. Choose from: {self.COLOURS}")
        # Using 'private' attributes by adding an underscore
        self._x = x
        self._y = y
        self._colour = colour

    @property
    def x(self):
        """
        Accessor for the x value
        :return: the value of _x
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Setter method for x — allows controlled changes to _x
        :param value: new x value
        :return: None
        """
        self._x = value

    @property
    def y(self):
        """
        Accessor for the y value
        :return: the value of _y
        """
        return self._y

    @property
    def colour(self):
        """
        Accessor for the colour value
        :return: the value of _colour
        """
        return self._colour

    @classmethod
    def add_colour(cls, colour):
        """
        Adds a new entry to the shared COLOURS list
        :param colour: new colour to add as a string
        :return: None
        """
        cls.COLOURS.append(colour)

    @staticmethod
    def from_tuple(coordinate, colour="red"):
        """
        Alternative constructor — builds an AdvancedPoint from a (x, y) tuple
        :param coordinate: tuple containing two numbers (x, y)
        :param colour: optional colour string (defaults to 'red')
        :return: AdvancedPoint instance
        """
        x, y = coordinate
        return AdvancedPoint(x, y, colour)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Computes the distance between two AdvancedPoint objects
        :param p1: first AdvancedPoint
        :param p2: second AdvancedPoint
        :return: distance as a float
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Calculates distance from this point to another AdvancedPoint
        :param p: another AdvancedPoint instance
        :return: distance as a float
        """
        return ((self.x - p.x) ** 2 + (self.y + p.y) ** 2) ** 0.5

# Example: adding a new colour to the COLOURS list via class method
AdvancedPoint.add_colour("rojo")

# Example: creating a new AdvancedPoint instance
p = AdvancedPoint(1, 2, "rojo")

# Changing x value directly (though typically this would use the setter)
p._x = 11

# Test: printing point and distance from origin
print(p)
print(p.distance_to_orig())

# Creating an AdvancedPoint using a tuple through the static method
p2 = AdvancedPoint.from_tuple((3, 2))

# Print new point
print(p2)

# Using static method to get distance between two points
print(AdvancedPoint.distance_2_points(p, p2))

# Using instance method to find distance from one point to another
print(p.distance_to_other(p2))
