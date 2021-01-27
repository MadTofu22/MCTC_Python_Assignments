''' Program: Problem #1 - Grade Level Calculator
    Author: Tom Stutler
    Last Date Modified: 9/28/14

    The intent of this program is to prompt the user for the number of credits they have completed and display their current grade level.
'''

#Prompt user for completed credits and assign to variable.
credits = int(input("Enter number of credits: "))

#Evaluate grade level and display result to user.
if credits < 32:
    print("Grade level: First year")

elif 32 <= credits <= 63:
    print("Grade level: Sophomore")

elif 64 <= credits <= 95:
    print("Grade level: Junior")

elif credits >= 96:
    print("Grade level: Senior")

######################################################################################

''' Program: Problem #2 - Highest/Lowest Score Finder
    Author: Tom Stutler
    Last Date Modified: 9/28/14

    The intent of this program is to prompt the user for three test scores, find the highest and lowest test scores, and display the result to the user.
'''

#Prompt user for test scores and assign to variables.
test1 = int(input("Enter first exam score: "))
test2 = int(input("Enter second exam score: "))
test3 = int(input("Enter third exam score: "))

#Find highest and lowest test scores and assign to variables.
highest = max(test1, test2, test3)
lowest = min(test1, test2, test3)

#Display highest and lowest test scores to user.
print("Highest score =", highest)
print("Lowest score =", lowest)

######################################################################################

''' Program: Problem #3 - Jesse Ventura Shirt Invoice Calculator
    Author: Tom Stutler
    Last Date Modified: 9/28/14

    The intent of this program is to prompt the user for a desired number of shirts they want to order, calculate the price of the shirts, shipping and handling fee, and the total cost, and display the results to the user.
'''

#Define function for calculation of shirt price.
def shirt_price_calc(qty):
    '''(int) -> float

    Return the price of the amount of shirts the user wants to order.

    Pricing tiers (per shirt):
    qty < 4 = $11.95
    4 <= qty < 8 = $9.95
    qty >= 8 = $7.95

    >>> shirt_price_calc(1)
    11.95
    >>> shirt_price_calc(6)
    59.70
    >>> shirt_price_calc(10)
    79.50
    '''

    if qty < 4:
        return qty * 11.95
    
    elif 4 <= qty < 8:
        return qty * 9.95

    elif qty >= 8:
        return qty * 7.95

#Define function for calculation of shipping and handling fee.
def ship_fee_calc(price):
    '''(float) -> float

    Return the shipping and handling cost based on the price of the shirts ordered.

    Shipping and handling fee structure:
    price <= 25.00 = $3.50
    25.01 <= price <= 75.00 = $5.95
    price >= 75.01 = $7.95

    >>> ship_fee_calc(11.95)
    3.50
    >>> ship_fee_calc(59.70)
    5.95
    >>> ship_fee_calc(79.50)
    7.95
    '''

    if price <= 25.00:
        return 3.50
    
    elif 25.01 <= price <= 75.00:
        return 5.95

    elif price >= 75.01:
        return 7.95

#Prompt user for number of shirts they want to order and assign to variable.
shirts_qty = int(input("Enter number of shirts: "))

#Calculate price of shirts and assign to variable.
shirts_price = round(shirt_price_calc(shirts_qty), 2)

#Calculate shipping and handling fee and assign to variable.
ship_fee = round(ship_fee_calc(shirts_price), 2)

#Calculate total cost to user and assign to variable.
total_price = shirts_price + ship_fee

#Display results to the user.
print("Total shirt cost = $" + str(shirts_price))
print("Shipping and handling = $" + str(ship_fee))
print("Total final cost = $%0.2f" % total_price)
