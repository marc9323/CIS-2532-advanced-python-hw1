"""
Marc D. Holman
CIS 2532 - Advanced Python Programming
Homework Assignment # 1
1 / 20 / 2020

Assignment Content:
'Shape.py' - Inheritance hierarchy based on abstract class
'main.py' - this file, main ( and supporting ) methods

"""

from Shape import Shape, Circle, Square, Cube
import random
from dataclasses import dataclass
from tkinter import messagebox
import matplotlib.pyplot as plt

#  Menu Item Constants
CONSOLE = 'a'
TEXT_FILE = 'b'
GUI = 'c'
QUIT = 'q'
FRESH = 'd'

#  total number of shapes to create
NUMBER_OF_SHAPES = 15

#  used to hold the total values for how many of each
#  shape were created
@dataclass
class ShapeCounter:
    circle: int
    square: int
    cube: int


def create_shape_list():
    """  create a list of shapes, with type for each shape being
    determined randomly.  Track total number of each type created
    return the list and the counter  """
    # list of shapes
    shapeList = []
    shapeCounter = ShapeCounter(0, 0, 0)
    for index in range(NUMBER_OF_SHAPES):
        # get a random number 1-3
        randNum = random.randrange(1, 4)
        #  choose a shape type based on randNum and append to the list
        if randNum == 1:
            shapeList.append(Circle())
            shapeCounter.circle += 1
        elif randNum == 2:
            shapeList.append(Square())
            shapeCounter.square += 1
        else:
            shapeList.append(Cube())
            shapeCounter.cube += 1

    return shapeList, shapeCounter


def create_shape_string(shapeList):
    """  create a string with shapes and volumes
    This string will be passed to console and file output
    methods """
    shapeString = "" #f"{'=' * 60}\n"
    for theShape in enumerate(shapeList):
        if not(isinstance(theShape[1], Cube)):
            theShape[1].find_area()
            shapeString += f"{theShape[0]},) {theShape[1].display()}\n"
        else:
            theShape[1].find_volume()
            shapeString += f"{theShape[0]},) {theShape[1].display()}\n"
    return shapeString


def output_shapestring_console(shapeString):
    """ display the list of shapes to the console """
    print("Assignment Number one (Shape List) output:\n\n")
    print(shapeString)


def output_shapestring_file(shapeString, filename):
    """  output the list of shapes to a text file """
    with open(filename, 'w') as theFile:
        theFile.write(shapeString)


def display_shape_gui(shapeList, shapeString):
    """  display the shape list and totals in a
    tkinter messagebox window"""
    messagebox.showinfo("SHAPE LIST", shapeString)


def display_pie_chart(shapeList, shapeCounter):
    """  show a pie chart for the number of each shape created """
    #  create a list of shape totals
    shapeTotals = [shapeCounter.circle, shapeCounter.square, shapeCounter.cube]
    #  create a list of labels for the slices
    slice_labels=['Circles', 'Squares', 'Cubes']
    # create a pie chart from the values
    plt.pie(shapeTotals, labels=slice_labels)
    #  add a title
    plt.title('Totals for Each Shape Type')
    #  display the pie chart
    plt.show()


def display_menu():
    """  display the text for the menu along with a header
    indicating the assignment number """
    print("Homework Assignment # 1 -- Abstract Classes and Polymorphism\n\n")
    print("All options create a list of shapes.")
    print("Please select from the following menu")
    print("To determine how you would like to see the data output:")
    print("A.)  display the results to the console")
    print("B.)  output the results to a text file")
    print("C.)  view the results inside a GUI messagebox")
    print("D.)  generate a fresh list of shapes")
    print("Q.)  Terminate the program, quit")


def input_menu_selection():
    """  get the menu selection from the user """
    choice = input("Your choice (1-3):")
    return choice


def input_shape_filename():
    """  get the filename for text file output from user """
    return input("Enter a filename please:  ")



def main():
    """  main method - main loop for the program """
    while True:
        #  get the list of shapes and totals
        shapeList, shapeCounter = create_shape_list()
        #  create a string which can be output to file, console, or gui
        shapeString = create_shape_string(shapeList)
        #  show the menu
        display_menu()
        #  get user selection
        choice = input_menu_selection().lower()  # make lowercase
        #  branch based on user selection
        if choice == CONSOLE:  # console output
            output_shapestring_console(shapeString)
            display_pie_chart(shapeList, shapeCounter)
        elif choice == TEXT_FILE:  #  output to text file
            filename = input_shape_filename()
            output_shapestring_file(shapeString, filename)
            display_pie_chart(shapeList, shapeCounter)
        elif choice == GUI:  # output to GUI
            display_shape_gui(shapeList, shapeString)
            display_pie_chart(shapeList, shapeCounter)
        elif choice == 'q':
            #  break out of the loop, program will terminate
            break
        else:
            print("Please make a valid selection.")





main()




