''' Program: Lab C #1
    Author: Tom Stutler
    Last Date Modified: 11/6/14

    The intent of this program is to prompt the user for the length and height of a rectangle,
    calculate the area, and display the length, height, and area to the user.
'''

def calculate_area(length, height):
    ''' (int, int) -> int

    The intent of this function is to take two integers,
    length and height of a rectangle, and calculate the area.

    >>> calculate_area(10, 5)
    50
    >>> calculate_are(25, 10)
    250
    '''

    return (length * height)

def main():
    ''' The intent of this function is to run bulk of the program,
    inlcuding prompting the user for the dimensions of the rectangle and displaying the results.
    '''

    #Prompt user for the dimensions of the rectangle and assign to variables.
    length = int(input("Please enter the length: "))
    height = int(input("Please enter the height: "))

    #Pass Dimensions through calculate_area and assign the reseult to a variable.
    area = calculate_area(length, height)

    #Display the result to the user.
    print("Length =", length)
    print("Height =", height)
    print("Area =", area)

#Call the main function to start the program.
main()

##################################################################################################################
''' Program: Lab C #2
    Author: Tom Stutler
    Last Date Modified: 11/6/14

    The intent of this program is to evaluate if a string is comprised of numbers, minus signs, and periods.
    If it is return True, if not return False.
'''

def isnumber(string):
    ''' (str) -> bool

    The intent of this funtion is to evaluate if a string has only numbers, minus signs, and periods.
    The return if that is True or False.

    >>> isnumber("65446")
    True
    >>> isnumber("-4456.6546")
    True
    >>> isnumber("A15saf")
    False
    '''

    #Assign a list containing all valid characters.
    valid_chars = ['-', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    #Check each character in string to see if it is valid.
    for index in string:
        if index in valid_chars:
            result = True
        else:
            result = False
            break
    return result

##################################################################################################################
''' Program: Lab C #3
'''

#Promp user for info.
name = input("Please enter your name: ")
year = input("Please enter your graduation year: ")
major = input("Please enter your major: ")

#Open a file and write name, year, and major to that file.
info = open('Lab_C_3.txt', 'w')
info.write(name + '\n' + year + '\n' + major)
info.close()

#Read the file back in and display to the user.
info = open('Lab_C_3.txt', 'r')
info_list = info.readlines()
for item in info_list:
    print(item)

##################################################################################################################
''' Program: Lab C #4
    Author: Tom Stutler
    Last Date Modified: 11/6/14
'''

def main():
    print("Party guest list program")
    party_guest = get_guest_data()
    filename = input("Enter filename to store data: ")
    write_guest_data(filename, party_guest)
    print("All Done. Thanks for using the program.")

def get_guest_data():

    list = []

    while True:
        guest = input("Please enter a guests name, or press enter to quit: ")
        if guest != '':
            list.append(guest)
        else:
            break
    return list
    
def write_guest_data(file, list):

    guest_file = open(file, 'w')
    for item in list:
        guest_file.write(item + '\n')
    guest_file.close()

main()
##################################################################################################################
''' Program: Lab C #5
    Author: Tom Stutler
    Last Date Modified: 11/6/14
'''

def main():
    print("Party guest list program")
    party_guests = get_guest_data()
    filename = input("Enter filename to store data: ")
    write_guest_data(filename, party_guests)
    print("All Done. Thanks for using the program.")

def get_guest_data():

    names = []
    numbers = []

    while True:
        guest = input("Please enter a guests name, or press enter to stop: ")
        
        if guest != '':
            phone = input("Please enter " + guest + "'s phone number, no hiphons or spaces: ")
            names.append(guest)
            numbers.append(phone)
        else:
            break
    data = dict(zip(names, numbers))
    return data
    
def write_guest_data(file, dictionary):

    guest_file = open(file, 'w')
    for item in dictionary:
        guest_file.write(item +' \t' + dictionary[item] + '\n')
    guest_file.close()

main()

##################################################################################################################
''' Program: Lab C #6
    Author: Tom Stutler
    Last Date Modified: 11/6/14

    The intent of this program is to take a list of students and break them up into groups.
'''
import random

def main():
    #Initialize variables and prompt user for how many groups they want.
    students = ["Ada Lovelace", "Bill Nye", "Catherine Deneuve", "Darth Vader", "Emily Dickenson", "F. Scott Fitzgerald", "George Clooney", "He-Man", "Incredible Hulk", "Josephine Baker", "Kanye West", "Lady Gaga", "Miley Cyrus"]
    groups_number = int(input("Enter how many groups you would like: "))
    groups_dictionary = assign_groups(students, groups_number)

    #Display the group list to the user.
    for name in students:
        print(name + ' is in group ' + str(groups_dictionary[name]))

    #Write the groups to a file.
    write_to_file(groups_dictionary)
    
def assign_groups(names, number):
    ''' (list, int) -> dict

    Takes a list of students and an integer of how many groups are wanted,
    and returns a dictionary with every studen assigned to a group.
    '''
    groups = {}
    for name in names:
        groups[name] = random.randrange(1, number+1)
    return groups

def write_to_file(dictionary):
    ''' Write the assigned groups to a file.
    '''

    filename = input("Please enter the file name you want to save your groups to: ")
    groups_file = open(filename, 'w')
    groups_file.write("Group \t Name \n")
    
    for key in dictionary:
        groups_file.write(str(dictionary[key]) + '\t' + key + '\n')

    groups_file.close()

main()
