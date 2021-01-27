''' Program: Loops Part 4 - Aproximate pi to User's discretion.
    Author(s): Tom Stutler
    Last Date Mofdified: 10/2/14

    The intent of this program is to prompt the user for how many iterations of Leibniz's pi aproximation they want to run, and display the result.
'''
import math

#Prompt user for how many iterations they want to run and assign to variable.
iterations = int(input("How many iterations would you like to aproximate? "))

#Assign base count for while loop.
count = 0
dividend = 3
aproximation = 1

#Run Leibniz's aproximation through the user specified amount of iterations.
while count < iterations:

    aproximation -= (1/dividend)
    dividend += 2
    aproximation += (1/dividend)
    dividend += 2
    count += 1

print("π = ", aproximation * 4)
