/*  Program: HW14 #5
    Author: Tom Stutler
    Last Date Modified: 12/15/14

    The intent of the program is to repeatedly prompt the user to enter an integer, until the hit enter to quit,
    then display the sum and average of entered integers.
*/

//Include modules and namespace
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    //Declare variables
    string currentTerm = "";
    int sum, counter, currentNum;

    //Define variables
    sum = 0;
    counter =0;

    //Start loop to continuously prompt user for input.
    while (true) {
        //Prompt user for input and store to variable
        cout << "Please enter a positive number or press enter to quit: ";
        getline(cin,currentTerm);

        //Check if input is valid, display result if not, continue loop if it is.
        if (currentTerm == "") {
            cout << "The sum of the numbers you entered is " << sum << " and the average is " << sum/counter << endl;
            return 0;
        }

        else {
            stringstream(currentTerm) >> currentNum;
            sum = sum + currentNum;
            counter++;
        }
    }
}
