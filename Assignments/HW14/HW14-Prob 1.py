''' Author: Tom Stutler
    Program: HW14 #2
    Last Date Modified: 12/8/14

    The intent of this program is to obtain 3 arc lengths from the user
    and calculate the radius of a circle, then return the answer to the user.
'''
#Import math to use PI
import math

def main():
    ''' Prompt user for 3 arc lengts of a circle, calculate the radius,
    and display it to the user.
    '''

    #Prompt user for input and store o variables.
    a = int(input("Enter the length of arc A: "))
    b = int(input("Enter the length of arc B: "))
    c = int(input("Enter the length of arc C: "))

    #Calculate the radius of the circle.
    radius = (a+b+c)/(2*math.pi)

    #Return the result to the user.
    print("The radius of your circle is", str(radius))

main()
