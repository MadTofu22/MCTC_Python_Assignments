''' Program: Loops Part 4 - Right Triangle Determination
    Author(s): TOm Stutler
    Last Date Modified: 10/2/14

    The intent of this program is to prompt the user to enter the length of the sides of a triangle and determing if it is a right triangle or not.
'''

#Prompt user for three sides and assign to variables.
side_a = int(input("Enter side A: "))
side_b = int(input("Enter side B: "))
side_c = int(input("Enter side C: "))

#Determine if the tirangle is a right triangle and return the result to the user.
if (side_a ** 2) + (side_b ** 2) == (side_c ** 2):
    print("You're triangle is a right triangle!")

else:
    print("You're triangle is not a right triangle.")
