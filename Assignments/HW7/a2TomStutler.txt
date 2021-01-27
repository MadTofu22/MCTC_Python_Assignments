''' Program: HW7 - DNA
    Author: Tom Stutler
    Last Date Modified: 10/12/14

    The intent of this program is to define several functions using strings of DNA sequnces in an attempt to better under stand the use and modification of python strings.
'''
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1) > len(dna2):
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    if dna != '' and nucleotide != '':
        nucleotide_count = 0
        for index in dna:
            if index == nucleotide:
                nucleotide_count += 1
        return nucleotide_count
    else:
        print("Please enter valid a valid DNA sequence and nucleotide.")


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    if dna1 != '' and dna2 != '':
        if dna2 in dna1:
            return True
        else:
            return False
    else:
        print("Please enter valid DNA sequences.")


def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence contains only 'A's, 'T's, 'C's,
    or 'G's and is not lower case.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGF')
    False
    '''
    if dna != '':
        for index in dna:
            if index == 'A' or index == 'T' or index == 'C' or index == 'G':
                valid_sequence = True
            else:
                valid_sequence = False
                break
        return valid_sequence
    else:
        return False


def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str

    Return a new DNA sequence in which dna2 has been instered into dna1
    at the specified index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', -1)
    'CCGATG'
    '''
    new_sequence = dna1[:index] + dna2 + dna1[index:]
    return new_sequence


def get_complement(nucleotide):
    ''' (str) -> str

    Return the complement of the given nucleotide. A and T are complents and
    C and G are complements.

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        print('Please enter a valid nucleotide.')

def get_complementary_sequence(dna1):
    ''' (str) -> str

    Return the complementary sequence to the DNA sequence provided.
    A and T are complements as well as C and G are complements.

    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complemetary_sequence('AAGG')
    'TTCC'
    '''
    dna2 = ''
    if dna1 != '':
        for index in dna1:
            if index == 'A':
                dna2 += 'T'
            elif index == 'T':
                dna2 += 'A'
            elif index == 'C':
                dna2 += 'G'
            elif index == 'G':
                dna2 += 'C'
            else:
                return 'Please enter a valid DNA sequence.'
                break
        return dna2
    else:
        print('Please enter a valid DNA sequence.')
