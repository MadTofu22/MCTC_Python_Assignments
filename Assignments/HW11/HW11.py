''' Program: HW11-#1
    Author: Tom Stutler
    Last Date Modified: 11/18/14

    The intent of this program is to prompt the user for an number, x, then aproximate the square route of x using Newton's algorithm.
'''

def main():

    user_num = float(input("Please enter the number you wish to find the square root of: "))
    significant_digits = 6
    original_estimate = 1
    final_estimate = aproximate_sqrt(user_num, original_estimate, significant_digits)

    print("The aproximate square root of", str(user_num), "is", str(final_estimate) + ".")
    

def aproximate_sqrt(number, estimate, tolerance):
    ''' (int, int, int) -> float

    The intent of this function is to aproximate the square root
    of a number to a specified tolerance, using Newton's algorithim, then return the estimate.

    >>> aproxmiate_sqrt(4, significant_digits)
    2.000000
    >>> aproximate_sqrt(5, significant_digits)
    2.236067
    '''

    variance = [number-10**(-tolerance),number, number+10**(-tolerance)]

    estimate = (estimate, tolerance)
    print(estimate)
    
    if estimate**2 in variance:
        return round(estimate, tolerance)
    else:
        estimate = ((estimate + (number/estimate))/2)
        aproximate_sqrt(number, estimate, tolerance)

main()
