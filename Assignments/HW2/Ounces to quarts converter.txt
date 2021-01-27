''' Program: Ounces to quarts converter
    Author: Tom Stutler
    Last date modified: 9/13/14

    The intent of this program is for the user to enter the desired amount of ounces to be converted quarts.'''

#Obtain users desired amount of ounces to convert.
ounces = int(input('How many ounces would you like convert? '))

#Calculate conversion and assign to variables.
quarts = ounces // 32
remainder = ounces % 32

#Display result to user.
print(ounces, 'oz. =', quarts, 'qt. and', remainder, 'oz.')
