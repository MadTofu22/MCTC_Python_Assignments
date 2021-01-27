/*
Program: HW14 #4
Author: Tom Stutler
Last Date Modified: 12/9/14

The intent of this program is to prompt the user to enter the dimensions
of a box (length, width, and height), calculate the surface area and volume,
and return the result to the user.

Pre-condition: User input must be entered in positive integers in inches.
*/

#include <iostream>

using namespace std;

int main()
{
    //Declare variables.
    int length, width, height;

    //Prompt user for input and define variables.
    cout << "Enter the length of the box: " << endl;
    cin >> length;
    cout << "Enter the width of the box: " << endl;
    cin >> width;
    cout << "Enter the height of the box: " << endl;
    cin >> height;

    //Display results to user.
    cout << "Box surface area = " << 2*(length*width + length*height + width*height) << " square inches." << endl;
    cout << "Box volume = " << length*width*height << " cubic inches." << endl;

    return 0;
}
