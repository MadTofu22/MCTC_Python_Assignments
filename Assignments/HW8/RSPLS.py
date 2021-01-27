''' Program: RSPLS
    Author: Tom Stutler
    Last date modified: 10/16/14

    The intent of this program is to have the user play a game of Rock, Paper, Sissors, Lizard, Spock! with the computer.
'''

#Imported modules
import random

def name_to_number(name):
    ''' (str) -> int

    Function receives the name of a choice made by the player
    or the computer, and converts it to it's assigned integer.

    0 <- rock
    1 <- Spock
    2 <- paper
    3 <- lizard
    4 - scissors

    >>> name_to_number('rock')
    0
    >>> name_to_number('Spock')
    1
    >>> name_to_number('')
    Please enter a
    valid choice.
    '''

    #if/elif/else statements to convert name to number.
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print("Please enter a valid choice.")
               

def number_to_name(number):
    ''' (int) -> str

    Function receives an integer of the player's or computers choice
    and returns the assigned name of that choice.

    0 —> rock
    1 —> Spock
    2 —> paper
    3 —> lizard
    4 —> scissors


    >>> number_to_name(3)
    lizard
    >>> number_to_name(0)
    rock
    >>> number_to_name(-3)
    Please enter a valid choice.
    '''

    #if/elif/else statements to convert number to name.
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print("Please enter a valid choice.")


def rpsls(player_choice):
    ''' (str) -> str, str, str

    This function takes in the players choice,
    generates the computers choice, decides the winner
    and displays the game to the user.
    '''

    #Convert player choice to it's integer value and assign it to a new variable.
    player_number = name_to_number(player_choice)

    #Generate the computers choice and assign it to a variable.
    comp_number = random.randrange(0,5)

    #Convert the computers choice to it's assign name value.
    comp_choice = number_to_name(comp_number)

    #Print the player's and the computers choice to the user, following a blank line to seperate games.
    print()
    print("Player chooses", player_choice)
    print("Computer chooses", comp_choice)

    #Decide the winner of the game and display it to the user.
    if (player_number - comp_number) % 5 == 1 or (player_number - comp_number) % 5 == 2:
        print("Player wins!")
    elif (player_number - comp_number) % 5 == 3 or (player_number - comp_number) % 5 == 4:
        print("Computer wins!")
    else:
        print("Player and Computer tie!")
