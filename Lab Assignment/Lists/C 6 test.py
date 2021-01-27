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
