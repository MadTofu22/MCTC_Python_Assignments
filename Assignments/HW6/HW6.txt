''' Progrogram: Problem #1 - Euclid's GCD Algorithm
    Author: Tom Stutler
    Last Date Modified: 10/5/14

    The intent of this program is to prompt the user for two integers, find the greatest common denominator, display the result to the user.
'''

#Prompt user for two numbers and assign to variables.
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

#Find the larger and smaller of the two numbers and assign to variables.
larger = max(num1, num2)
smaller = min(num1, num2)

#Display short explanation of Euclid's algorithm to the user
print('To find the GCD (greatest common denominator)\ndivide the larger number by the smaller number,\nreplace the larger with the smaller and the smaller with the remainder.\nRepeat the process until the remainder is 0.')

#Create loop to find the GCD.
while 1 == 1:

    if smaller == 0:
        gcd = larger
        break

    elif smaller != 0:
        remainder = larger % smaller
        print(str(larger) + '/' + str(smaller), '=', larger//smaller, 'with', remainder, 'remaining.')
        larger = smaller
        smaller = remainder

#Display the resulting GCD to the user.
print('The GCD of', num1, 'and', num2, 'is', str(gcd) + '.')

########################################################################################################################################################################################################################################

''' Program: Problem #2 - Numbers List
    Author: Tom Stutler
    Last Date Modified: 10/6/14

    The intent of this program is to prompt the user to input a list of numbers seperated by a space, then find the sum and average of the numbers, and display the results to the user.
'''

#Prompt user for a list of numbers seperated by a space and assign to a variable.
string = input('Enter a list of numbers, seperate each number by a space: ')

#Convert string to a list of integers.
nums = map(int, string.split())
nums = list(nums)

#Calculate the sum and and average of the list nums.
print(sum(nums))
print(sum(nums)/len(nums))

########################################################################################################################################################################################################################################

''' Program: Problem #3 - Delivery Charge Calculator
    Author: Tom Stutler
    Last Date Modified: 10/6/14

    The intent of this program is to prompt the user for the weight of a package, in ounces, calculate the delivery charge, $3.50 + $0.50((w-13)//4), and display the weight in pounds and ounces and the delivery charge.
'''

def get_weight():
    #Prompts the user for a weight in ounces, and passes it through the delivery_charge function.
    weight = int(input('Enter the weight of your package, in ounces: '))
    delivery_charge(weight)

def delivery_charge(weight):
    ''' (int) -> float

    Takes in the weight of a package and calculates the delivery charge, then passes the weight and the delivery charge through the display_charge funcion.

    delivery_charge(16)
    >>> 3.50
    delivery_charge(23)
    >>> 4.50
    '''

    charge = 3.50
    charge += 0.5 * float((weight - 13)//4)
    display_charge(weight, charge)

def display_charge(weight, charge):
    #Display the package weight in ounces and pounds and the calculated delivery charge to the user.
    print('Package weight =', (weight//16), 'lb.', (weight%16), 'oz.')
    print('Delivery charge = $%0.2f' %charge)

def main():
    #Initiates the program.
    get_weight()

main()
