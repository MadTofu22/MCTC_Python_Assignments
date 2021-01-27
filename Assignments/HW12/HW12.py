''' Program: CSCI 1500 HW12
    Author: Tom Stutler
    Last Date Modified: 12/1/14

    The intent of this program is to allow the user to enter a shape and dimension
    display the perimeter to the user.
'''

#Imports
import math

def main():

    #Prompt user to select shape, convert to int, and store to variable.
    shape = input("Select shape (1=circle, 2=rectangle, 3=triangle, other to exit): ")

    #Determine what shape function to call, ask for it's dimensions, then display the calulated perimeter.
    if shape == '1':
        diameter = float(input("Enter circle diameter: "))
        perimeter = circle(diameter)
        print("Perimeter =", str(perimeter))

    elif shape == '2':
        dimensions = (input("Enter rectangle length and width: ")).split()

        #Check valid dimensions.
        if len(dimensions) == 2:
            length = float(dimensions[0])
            width = float(dimensions[1])
            perimeter = rectangle(length, width)
            print("Perimeter =", str(perimeter))
        else:
            print("Please enter valid dimension.")
            main()

    elif shape == '3':
        dimensions = (input("Enter triangle side lengths: ")).split()

        #Cehck valid dimensions.
        if len(dimensions) == 3:
            a = float(dimensions[0])
            b = float(dimensions[1])
            c = float(dimensions[2])
            perimeter = triangle(a, b, c)
            print("Perimeter =", str(perimeter))
        else:
            print("Please enter valid dimension.")
            main()
    else:
        print("Bye...")
        return    

    #Recall main to reprompt user.
    main()
    

def circle(d):
    ''' (float) -> float

    The intent of this function is to determine the perimiter of a circle, with
    positive diameter d, and return the perimeter.

    >>> circle(10)
    31.4159
    >>> circle(5)
    15.707963267948966
    '''

    perim = math.pi * d
    return perim


def rectangle(l, w):
    ''' (float) -> float

    The intent of this function is to determine the perimeter of a rectangle,
    with positive dimensions l and w, and return the perimeter.
    >>> rectangle(2.5, 7)
    19.0
    >>> rectangle(5, 10)
    15.0
    '''

    perim = (2*l)+(2*w)
    return perim

def triangle(a, b, c):
    ''' (float, float, float) -> float

    The intent of this function is to determine the perimeter of a trangle,
    with positive dimensions a, b, and c, and return the perimeter.

    >>> triangle(5, 5, 5)
    15
    >>> triangle(3, 4, 5)
    12.0
    '''

    perim = a+b+c
    return perim

main()
