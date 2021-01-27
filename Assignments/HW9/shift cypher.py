def shift_cypher(string, shift):
    ''' (str, int) -> str

    The purpose of this function is to take in a string and an integer to shift the string by
    through the alphabet. If shifted by 1 A becomes B and Z becomes A. Once the string has been shifted
    return the new string back.

    >>> shift_cypher('cheer', 7)
    'jolly'
    >>> shift_cypher('melon', -10)
    'cubed'
    '''

    #Initialize variables
    string_shifted = ''
    alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
    
    #Change the letters in string by the new values in alphabet_shift to create string_shifted
    for index in string:
        value = alphabet[index]
        for key_shift in alphabet:
            if alphabet[key_shift] == (value+shift)%26:
                 string_shifted += key_shift

    #Return the result
    return string_shifted
