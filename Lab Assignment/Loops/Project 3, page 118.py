'''Program: Loops Part 4 – Guess my number machine!
   Author(s): Tom Stutler
   Last Date Modified: 10/2/14

   The intent of this program is to have the user enter two numbers. The program then generates a random number bewtween the two user entered numbers and prompts the user to guess the randomly generated number. If the guess is incorrect it will tell tell the user “Too small” or “To large”. Once the user guesses correctly it will tell them they’re correct and how many guesses it took.
'''

import random

#Prompt the user to enter the larger and smaller limits and the number they want the computer to guess, then assign to variables.
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = int(input("Enter the number you want the computer to guess (minimum 3 guesses): "))

#Sets the amount of guess the computer has.
guesses = [1, 2, 3]

for guess in guesses:

    #Computer guesses a number and assigns to variable.
    machineNumber = random.randint(smaller, larger)
    if machineNumber < myNumber:
        print("Too small")
        
    elif machineNumber > myNumber:
        print ("Too large")
        
    elif machineNumber == myNumber:
        print("Unfortunataly the machine bested you and guessed your number. You lose.")
        break
    
if machineNumber != myNumber:
    print("The computer was unable to guess your number. You win!")
