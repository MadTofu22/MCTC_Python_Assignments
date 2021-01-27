''' Program: Change counter
    Auhor: Tom Stutler
    Last date modified: 9/13/14

    The intent of this program is to allow the user to enter the quanties of each US coin they have, tally the bananas, and display the total amount of currency.'''

#Obtain quantity of each coin type from the user and assign to variable.
quarters = int(input('How many quarters do you have?'))
dimes = int(input('How many dimes do you have?'))
nickels = int(input('How many nickels do you have?'))
pennies = int(input('How many pennies do you have?'))

#Calculate the total USD amount for each coin, and the total USD for all coins, and assign to variable.
quarters_total = quarters * 0.25
dimes_total = dimes * 0.1
nickels_total = nickels * 0.05
pennies_total = pennies * 0.01
total_all = quarters_total + dimes_total + nickels_total + pennies_total

#Display the result to the user.
print(quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels, and', pennies, 'pennies = $' + str(total_all))
