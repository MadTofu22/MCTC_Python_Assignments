"""
Program: Problem #3 – Draw a card!
Author(s): Tom Stutler, Seth Stoxen, Ashton Kelley
Last Date Modified: 09-30-14

This program will ask a player if they want a card. If som it will generate a random card with card face and suit names included. It will then ask them if they want another card or not.
"""

import random

def draw_card():
    """This is the function to choose a card."""
    #Retry gets reassigned at the end of the upcoming while loop.
    retry = input("Would you like to draw a card?")

    #This loops around if the person wants a different card at the end.
    while retry == "y":
        #This chooses a random number from 1-13 and then assigns it to a card.
        cardNum = random.randint(1, 13)
        if cardNum == 1:
            cardNum = str("Ace")
        if cardNum == 11:
            cardNum = str("Jack")
        if cardNum == 12:
            cardNum = str("Queen")
        if cardNum == 13:
            cardNum = str("King")
        #This chooses a random number from 1-4 and then assigns it to a suit.
        cardSuit = random.randint(1, 4)
        if cardSuit == 1:
            cardSuit = str("Hearts")
        if cardSuit == 2:
            cardSuit = str("Diamonds")
        if cardSuit == 3:
            cardSuit = str("Spades")
        if cardSuit == 4:
            cardSuit = str("Clubs")
        print ("Your card is the", cardNum, "of", cardSuit,)
        retry = input("Would you like a different card? (y/n)")
        #this takes the input from the retry variable to decide if it wants to start over or not. It will start over if they say y but break if they input n. Anything else will result in yelling at them and then starting over anyway.
        if retry == "y":
            True
        elif retry == "n":
            break
        else:
            print ("You need to enter 'y' or 'n'")
            main()

def main():
    """This is to get the whole thing started. Its existence is to be able to loop if the user doesnt enter a 'y' or an 'n' at the end of the drawn_card function."""
    draw_card()

main()
