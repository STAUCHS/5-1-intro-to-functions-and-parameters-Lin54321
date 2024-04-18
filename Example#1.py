#-------------------------------------------------------------------------
# Name:		    Lesson 5.1 Intro to Functions & Parameters
# Purpose:		Example #1
# Author:		Lin. H
# Created:		18/04/2024
#-------------------------------------------------------------------------

# Example #1:
## Part (a) Create a function that will calculate the area of a rectangle
# length = float(input("Enter the length (in cm): "))
# width = float(input("Enter the width (in cm): "))

# area = length * width

# print(f"The area of the rectangle is: {area} cm^2")

def rect_area(length: float, width: float):
    area = length * width
    print(area)

## Part (b) Use your function by calling it
rect_area(4, 5)