''' Program: Problem #1 - I got a dollar!
    Author(s): Tom Stutler, Seth Stoxen, Ashton Kelley
    Last Date Modified: 9/29/14

    The intent of this program is to prompt the user for a number of cents they have and return whether or not they have a dollar.
'''

#Define function to see if you have less than a dollar, exactly one dollar, or you have more than a dollar.
def dollar(cents):
    if cents > 100:
        print ("You have more than one dollar!")

    elif cents == 100:
        print ("You have exactly one dollar!")

    elif 0 < cents < 100:
        print ("You don't quite have a dollar.")
    else:
        print ("Please retry and enter a positive amount of cents.")

#Prompt user for the amount of cents they have and assign to a variable.
cents = int(input("Enter how many cents you have: "))

#Use dollar() to calculate how many dollars, if any, the user has.
dollar(int(input("Enter how many cents you have: ")))
