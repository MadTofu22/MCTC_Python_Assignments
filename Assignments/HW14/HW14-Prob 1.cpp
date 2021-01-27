/*
Author: Tom Stutler
Program: HW14 #2
Last Date Modified: 12/8/14

The intent of this program is to obtain 3 arc lengths from the user
and calculate the radius of a circle, then return the answer to the user.
*/
#include <iostream>

using namespace std;

int main ()
{
    //Declare variables and define constants.
    double a, b, c, radius;
    const double PI = 3.14593;

    //Prompt user for arc lengths and store to variables.
    cout << "Enter the length of arc a: " << endl;
    cin >> a;
    cout << "Enter the length of arc b: " << endl;
    cin >> b;
    cout << "Enter the length of arc c: " << endl;
    cin >> c;

    //Calculate the radius and store to variable.
    radius = (a+b+c)/(2*PI);

    //Output the result to the user.
    cout << "The radius of the circle is " << radius << endl;
    return 0;
}
