##########################
#Cracking the Coding Interview
#Page9 90
#Question 1.1
###############################


"""Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
    
    >>> is_unique("noon")
    False

    >>> is_unique("dog")
    True
"""

def is_unique(str):
    """Return True/False if all characters are unique"""

    #loop through string and append each char to lst and check if it exists in lst already

    char_seen = []

    for char in str:
        if char in char_seen:
            return False
        char_seen.append(char)

    return True




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** All Tests Passed"