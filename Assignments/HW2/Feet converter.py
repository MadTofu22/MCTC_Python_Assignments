''' Program: Feet converter
    Author: Tom Stutler
    Last date modified: 9/13/14

    The intent of this program is to convert the users entered feet into other various units of measurements.'''

#Obtain desired feet to be converted from user and assign to a variable.
feet = int(input('How many feet would you like to convert? '))

#Calculate conversions and assign to new variables.
yards = round(feet/3, 3)
inches = round(feet*12, 3)
cm = round(inches*2.54, 3)
meters = round(cm/100, 3)

#Display result to user.
print('The requested number of feet have been converted and rounded to 3 decimal places.')
print(feet, 'feet =', yards, 'yards,', inches, 'inches,', cm, 'centimeters, and', meters, 'meters.')
