##########################
#Cracking the Coding Interview
#Page 90
#Question 1.2
###############################


"""Given two strings, write a method to decide if one if a permutation of the other
    
    >>> is_permutation("earth", "heart")
    True

    >>> is_permutation("mom", "moo")
    False
"""

def is_permutation(str1, str2):
    """Return True/False if all characters are unique"""

    # add both strings to dict and compare.

    dict_1 = {}
    dict_2 = {}

    for char in str1:
        dict_1[char] = dict_1.get(char, 0) + 1

    for char in str2:
        dict_2[char] = dict_2.get(char, 0) + 1


    return dict_1 == dict_2




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** All Tests Passed"