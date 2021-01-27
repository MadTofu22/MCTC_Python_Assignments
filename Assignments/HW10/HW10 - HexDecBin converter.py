''' Program: HW 10
    Author: Tom Stutler
    Last Date Modified: 11/12/14

    The intent of this program is to create functions that test
    the various coversions we learned in our number systems topic.
'''

#Define lookup tables.
hexToBinaryTable = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
binaryToHexTable = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7', '1000':'8', '1001':'9', '1010':'A', '1011':'B', '1100':'C', '1101':'D', '1110':'E', '1111':'F'}
decToHexTable = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
hexToDecTable = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'}

def hexToBinary(number, table):
    ''' (str, dict) -> str

    The intent of this function is to take a number in hexidecimal form
    and a dictionary to convert from hex to binary.

    >>> hexToBinary('F', hexToBinaryTable)
    '1111'
    >>>> hexToBinary('9', hexToBinaryTable)
    '1001'
    >>> hexToBinary('FA1', hexToBinaryTable)
    '111110100001'
    '''

    #Initialize return variable.
    newNumber = ''

    #Convert number to newNumber
    for index in number:
        newNumber += table[index]

    #Return the binary number
    return newNumber

def binaryToHex(number, table):
    ''' (str, dict) -> str

    Precondition: Number must be a series of 4-bit binary digits, including leading 0's.

    The intentof this function is to take a number in binary form and a
    dictionary to convert the number from binary to hex.

    >>> binaryToHex('1111', binaryToHexTable)
    'F'
    >>> binaryToHex('1001', binaryToHexTable)
    '9'
    >>> binaryToHex('111110100001', binaryToHexTable)
    'FA1'
    '''
    
    #Initialize variables.
    newNumber = ''
    sliceCount = (len(number)//4)
    sliceNum1 = 0
    sliceNum2 = 4
    loopCount = 0

    #Convert number to newNumber.
    while loopCount < sliceCount:
        newNumber += table[number[sliceNum1:sliceNum2]]
        loopCount += 1
        sliceNum1 += 4
        sliceNum2 += 4

    #Return the hex number.
    return newNumber

def decimalToHex(number, table):
    ''' (str, dict) -> str

    The intent of this function is to take a number in decimal form and a dictionary
    to convert the number to hex.

    >>> decimalToHex('128', decToHexTable)
    'F0'
    >>> decimalToHex('6921', decToHexTable)
    '1B09'
    >>> decimalToHex('999999999', decToHexTable)
    'B9AC9FF'
    '''

    #Initialize variables.
    newNumber = ''
    dividend = int(number)//16
    remainder = int(number)%16

    #Convert the number to newNumber.
    while True:
        if dividend == 0 and remainder == 0:
            break
        else:
            newNumber = table[str(remainder)] + newNumber
        
        remainder = dividend%16
        dividend = dividend//16

    #Return the hex number.
    return newNumber

def hexToDecimal(number, table):
    ''' (str, dict) -> str

    The intent of this function is to take a number in hexidecimal form and a dicyionary
    and convert it to decimal.

    >>> hexToDecimal('F0', hexToDecTable)
    '240'
    >>> hexToDecimal('1B09', hexToDecTable)
    '6921'
    >>> hexToDecimal('3B9AC9FF', hexToDecTable)
    '999999999'
    '''

    #Initialize variables.
    power = len(number)-1
    newNumber = 0

    #Convert number to newNumber.
    for index in number:
        newNumber += int(table[index])*(16**power)
        power -= 1

    #Return the decimal number.
    return str(newNumber)

def binaryToDecimal(number):
    ''' (str) -> str

    The intent of this function is to take a binary number and convert it to decimal.

    >>> binaryToDecimal('111110100001')
    '4001'
    >>> binaryToDecimal('1101100001001')
    '6921'
    >>> binaryToDecimal('1111')
    '15'
    '''

    #Convert number to decimal.
    hexNumber = binaryToHex(number, binaryToHexTable)
    decNumber = hexToDecimal(hexNumber, hexToDecTable)

    return decNumber

def decimalToBinary(number):
    ''' (str) -> str

    The intent of function is to take a decimal number and convert it to binary.

    >>> decimalToBinary('4001')
    '111110100001'
    >>> decimalToBinary('6921')
    '1101100001001'
    >>> decimalToBinary('15')
    '1111'
    '''

    #Convert number to binary.
    hexNumber = decimalToHex(number, decToHexTable)
    binaryNumber = hexToBinary(hexNumber, hexToBinaryTable)

    return binaryNumber

def main():

    #Test first function.
    print("test hexToBinary('3FB', hexToBinaryTable) should be 001111111011")
    print(hexToBinary('3FB', hexToBinaryTable))

    #Test second function.
    print("test binaryToHex('001111111011', binaryToHexTable) should be 3FB")
    print(binaryToHex('001111111011', binaryToHexTable))

    #Test third function.
    print("test decimalToHex('2530', decToHexTable) should be 9E2")
    print(decimalToHex('2530', decToHexTable))

    #Test fourth function.
    print("test hexToDecimal('9E2', HexDecTable) should be 2530")
    print(hexToDecimal('9E2', hexToDecTable))

    #Test fifth function.
    print("test binaryToDecimal('100111100010') should be 2530")
    print(binaryToDecimal('100111100010'))

    #Test sixth function.
    print("test decimalToBinary('2530') should be 100111100010")
    print(decimalToBinary('2530'))

main()
