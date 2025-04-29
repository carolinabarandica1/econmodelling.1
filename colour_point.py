from point import Point
import random

class ColourPoint(Point):
    def __init__(self, x, y, colour):
        """
        Creates a ColourPoint object. Checks that x and y are numbers before setting values.
        :param x: numeric value for x position
        :param y: numeric value for y position
        :param colour: string representing the colour name
        """
        if not isinstance(x, (int, float)):  # Check if x is a number
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):  # Check if y is a number
            raise TypeError("y must be a number")

        # Call the parent class constructor to assign x and y
        super().__init__(x, y)
        self.colour = colour  # Assign colour to the instance

    def __str__(self):
        """
        Defines how the object should be displayed when printed.
        :return: string with colour and coordinates
        """
        return f"<{self.colour}: {self.x}, {self.y}>"

if __name__ == "__main__":
    p = ColourPoint(1, 2, "red")

    # Show distance from origin using inherited method
    print(p.distance_to_orig())

    # Display the ColourPoint object
    print(p)

    # Example: list of colours for testing
    # colours = ["red", "green", "blue", "yellow", "black", "magenta",
    #            "cyan", "white", "burgundy", "periwinkle", "marsala"]

    # Example: creating a list of random ColourPoint instances
    # colour_points = []
    # for i in range(10):
    #     colour_points.append(
    #         ColourPoint(random.randint(-10, 10),  # Random x between -10 and 10
    #                     random.randint(-10, 10),  # Random y between -10 and 10
    #                     random.choice(colours)))  # Pick a random colour from the list

    # Print the list of ColourPoint objects
    # print(colour_points)

    # Example: sorting ColourPoint objects based on distance from origin
    # colour_points.sort()
    # print(colour_points)
