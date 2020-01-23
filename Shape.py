"""
Marc D. Holman
CIS 2532 - Advanced Python Programming
Homework Assignment # 1
1 / 20 / 2020

Contents:
Enum class for Color

Circle, Square, and Cube which subclass Shape,
Shape2D and Shape3D

"""

from abc import ABC, abstractmethod, abstractproperty
from math import pi
from aenum import Enum  #  pip install aenum


class Color(Enum):
    RED = 1, "red"
    GREEN = 2, "green"
    YELLOW = 3, "yellow"
    BLUE = 4, "blue"
    PURPLE = 5, "purple"


class Shape(ABC):
    """ Abstract base class for Shape hierarchy"""

    def __init__(self, color=Color.RED):
        self.__color = color

    @abstractmethod
    def find_area(self):
        """ abstract method - implementation calculates area """
        pass

    @abstractmethod
    def find_volume(self):
        """  abstract method - implementation calculates volume"""
        pass

    @abstractmethod
    def display(self):
        """abstract method - implementations will display Shape name and area """
        pass

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Circle(Shape):
    """  Circle class inherits from abstract class Shape"""
    def __init__(self, radius=1, color=Color.RED):
        super().__init__(color)
        #  use the setter so as not to duplicate validation code
        self.set_radius(radius)

    def find_area(self):
        """ area for a circle:  pi * radius squared"""
        self.__area = pi * (self.__radius ** 2)
        return self.__area

    def find_volume(self):
        """  a circle has no volume"""
        pass

    def get_radius(self):
        """ getter returns radius of the circle """
        return self.radius

    def set_radius(self, radius):
        """ validate and set radius for the circle
        call find_area - class keeps area valid """
        if radius > 0:
            self.__radius = radius
            # keep the area up to date
            self.find_area()
        else:
            raise ValueError("Please provide positive radius")

    #  Override
    def display(self):
        """ display Shape name and area """
        #  use __class__.__name__ so code works if we change the name
        #  of our class
        return f"{self.get_color().name} Circle with area {self.__area:.2f}"


class Square(Shape):
    """ Square class inherits from abstract class Shape """
    def __init__(self, side=2.3, color=Color.RED):
        super().__init__(color)
        self.set_side(side)

    def find_area(self):
        """ area for a square is side length squared"""
        self.__area = self.__side ** 2
        return self.__area

    def find_volume(self):
        """ square has no volume """
        pass

    def get_side(self):
        """ getter returns length of square sides """
        return self.__side

    def set_side(self, side):
        """ validate and set side length
        call find_area - class keeps area valid"""
        if side > 0:
            self.__side = side
            self.find_area()
        else:
            raise ValueError("Please provide a positive side length")

    # Override
    def display(self):
        """ displays data for the shape """
        return f"{self.get_color().name} Square with area {self.__area:.2f}"


#  for a cube the lenth, width, and height are all the same
class Cube(Shape):
    """ Cube class inherits from abstract class Shape """
    NO_OF_SIDES = 6 # a cube has six sides

    def __init__(self, edge=1, color=Color.RED):
        super().__init__(color)
        self.set_edge(edge)

    def get_edge(self):
        return self.__edge

    def set_edge(self, edge):
        """ validate and set edge length
        call find_volume - keep value valid """
        if edge > 0:
            self.__edge = edge
            self.find_volume()
            self.find_area()
        else:
            raise ValueError("Side of a cube must be positive")

    def find_area(self):
        """ a = 6l^2"""
        self.__area = self.NO_OF_SIDES * (self.__edge ** 2)
        return self.__area

    def find_volume(self):
        """ volume for a cube is edge cubed """
        self.__volume = self.__edge ** 3
        return self.__volume

    # Override
    def display(self):
        return f"{self.get_color().name} Cube with volume {self.__volume:.2f}"


a = Circle(color=Color.GREEN)
b = Square(color=Color.BLUE)
# b = Cube(color=Color.BLUE)
print(b.display())
a.set_color(Color.RED)
print(a.get_color().value)

