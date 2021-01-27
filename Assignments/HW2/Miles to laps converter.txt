''' Program: Miles to laps converter
    Author: Tom Stutler
    Last date modified: 9/12/14

    The intent of this program is to allow the user to convert the amount of miles desired to run into laps aound a specified track.'''

miles = int(input("How many miles would you like to run?")) #Ask user for desired miles and assign to variable.
laps = miles * 14 #Convert miles into the required amount of laps and assign to variable.
print('To complete', miles, 'mile(s), you need to run', laps, 'lap(s) around the track.') #Display the result of the conversion.
