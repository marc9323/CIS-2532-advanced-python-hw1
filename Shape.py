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
from enum import Enum


class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    YELLOW = 'Yellow'
    BLUE = 'Blue'
    PURPLE = 'Purple'


class Shape(ABC):
    """ base abstract class for Shape hierarchy"""
    @abstractmethod
    def __init__(self, color=Color.RED):
        pass

    @abstractmethod
    def display(self):
        """ display, override in concrete subclasses """
        pass


class Shape2D(Shape):
    """ abstract class for 2 dimensional shapes """
    def __init__(self, color=Color.RED):
        self.__color = color

    @abstractmethod
    def find_area(self):
        """  override in concrete subclasses """
        pass

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Shape3D(Shape):
    """  abstract class for 3 dimensional shapes """

    def __init__(self, color=Color.RED):
        self.__color = color

    @abstractmethod
    def find_volume(self):
        """  override in concrete subclasses """
        pass

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


class Circle(Shape2D):
    """  Circle class inherits from abstract class Shape"""
    def __init__(self, radius=1, color=Color.RED):
        super().__init__(color)
        #  use the setter so as not to duplicate validation code
        self.set_radius(radius)

    def find_area(self):
        """ area for a circle:  pi * radius squared"""
        self.__area = pi * (self.__radius ** 2)

    def get_radius(self):
        """ getter returns radius of the circle """
        return self.radius

    def set_radius(self, radius):
        """ validate and set radius for the circle """
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
        return f"Circle with area {self.__area:.2f}"


class Square(Shape2D):
    """ Square class inherits from abstract class Shape """
    def __init__(self, side=2.3, color=Color.RED):
        super().__init__(color)
        self.set_side(side)

    def find_area(self):
        """ area for a square is side length squared"""
        self.__area = self.__side ** 2

    def get_side(self):
        """ getter returns length of square sides """
        return self.__side

    def set_side(self, side):
        """ validate and set side length """
        if side > 0:
            self.__side = side
            self.find_area()
        else:
            raise ValueError("Please provide a positive side length")

    # Override
    def display(self):
        """ displays data for the shape """
        return f"Square with area {self.__area:.2f}"


#  for a cube the lenth, width, and height are all the same
class Cube(Shape3D):
    """ Cube class inherits from abstract class Shape """
    def __init__(self, edge=1, color=Color.RED):
        super().__init__(color)
        self.set_edge(edge)

    def get_edge(self):
        return self.__edge

    def set_edge(self, edge):
        if edge > 0:
            self.__edge = edge
            self.find_volume()
        else:
            raise ValueError("Side of a cube must be positive")

    def find_volume(self):
        """ volume for a cube is edge cubed"""
        self.__volume = self.__edge ** 3

    # Override
    def display(self):
        return f"Cube with volume {self.__volume:.2f}"


a = Circle(color=Color.GREEN)
a.set_color(Color.RED)
print(a.get_color().value)

