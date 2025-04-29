import random

class Point:
    def __init__(self, x, y):
        """
        Constructor to create a new Point instance.
        :param x: numeric value for the x-axis
        :param y: numeric value for the y-axis
        """
        self.x = x  # Assign x-coordinate to the object
        self.y = y  # Assign y-coordinate to the object

    def __str__(self):
        """
        Special method that returns a readable string when printing the object.
        :return: string displaying x and y values
        """
        return f"<x={self.x}, y={self.y}>"

    def __repr__(self):
        """
        Special method that defines how the object looks when printed in a list or console.
        :return: same result as __str__()
        """
        return self.__str__()

    def distance_to_orig(self):
        """
        Computes how far the point is from the origin (0, 0)
        :return: distance using the Pythagoras theorem
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        Special method to compare two points based on their distance to the origin.
        :param other: another Point instance
        :return: True if self is further from origin than other, else False
        """
        my_distance = self.distance_to_orig()
        other_distance = other.distance_to_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Special method to check if two points are at the same distance from the origin.
        :param other: another Point instance
        :return: True if both distances are equal, else False
        """
        my_distance = self.distance_to_orig()
        other_distance = other.distance_to_orig()
        return my_distance == other_distance

if __name__ == "__main__":
    # Create instances of Point
    p = Point(1, 2)
    p2 = Point(2, 3)
    p4 = Point(1, -55)

    # Show attribute values
    print(f"p.x={p.x} & p.y={p.y}")
    print(f"p4.x={p4.x} & p4.y={p4.y}")

    # Change attribute value after creation
    p.x = 20
    print(f"p.x={p.x} & p.y={p.y}")

    # Display object using the custom __str__ method
    print(p)

    # Generate and display a list of 5 random Point objects
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10),
                            random.randint(-10, 10)))

    print("Generated these random points:")
    for point in points:
        print(point)

    print(points)  # When printed as a list, uses __repr__

    # Example of distance calculation
    p = Point(3, 4)
    print(p.distance_to_orig())

    # Example of comparison between two points
    p2 = Point(1, 1)
    print(f"Is p further than p2 from origin? {p > p2}")
    print(f"Do p and p2 have the same distance from origin? {p == p2}")

    # Sorting a list of points by their distance to origin
    print("Sorted list of points by distance to origin:")
    points.sort()
    print(points)
