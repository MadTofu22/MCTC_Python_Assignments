//include statement(s)
#include <iostream>
#include <string>

//using namespace statement
using namespace std;

int main()
{
    //variable declaration
    int SECRET, num1, num2, newNum;
    double RATE, hoursWorked, wages;
    string name;

    //executable statements
    SECRET = 11;
    RATE = 12.50;
    num1 = 15;
    num2 = 28;
    newNum = (num1*2)+num2;
    name = "Tom Stutler";
    hoursWorked = 45.50;
    wages = RATE*hoursWorked;

    //return statement
    cout << "The value of num1 = " << num1 << "and the value of num2 = " << num2 << endl;
    cout << "The value of newNum = " << newNum << endl;
    cout << "The new value of newNum = " << newNum+SECRET << endl;
    cout << "Name: " << name << endl;
    cout << "Pay Rate: $" << RATE << endl;
    cout << "Hours Worked: " << hoursWorked << endl;
    cout << "Salary: $" << wages << endl;
}
