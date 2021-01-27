''' Program: Volume and surface area finder
    Author: Tom Stutler
    Last date modified: 9/12/14

    The intent of this program is to obtain the dimensions of a box from the user then calculate and return the volume and surface area of said box.'''

#Obtain dimension from the user and assign to respective variables.
l = int(input('Please enter the length of the box in inches: '))
w = int(input('Please enter the width of the box in inches: '))
h = int(input('Please enter the height of the box in inches: '))

#Calculate the surface area and volume of the box and assign to variables.
area = 2 * (l*w + l*h + w*h)
volume = l*w*h

#Display the output to the user.
print('Box surface area =', area, 'square inches.')
print('Box volume =', volume, 'cube inches.')
