#-------------------------------------------------------------------------
# Name:		    Lesson 5.1 Intro to Functions & Parameters
# Purpose:		Example #2
# Author:		Lin. H
# Created:		18/04/2024
#-------------------------------------------------------------------------

# Example #1:
## Part (a) Create a function that will check if a number is even or odd
num = int(input("Enter a number: "))

def even_odd(num: int):
    if num == 0:
        print("0 is neither even nor odd.")
    elif num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

## Part (b) Use your function by calling it
even_odd(num)