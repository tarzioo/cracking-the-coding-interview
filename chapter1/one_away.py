##########################
#Cracking the Coding Interview
#Page 91
#Question 1.5
###############################


"""There are three types of edits, insert a char, remove a char ore replce a char."
    
    >>> one_away("pale", "ple")
    True

    >>> one_away("pales", "pale")
    True

    >>> one_away("pale", "bale")
    True

    >>> one_away("pale", "bake")
    False

"""

def one_away(str1, str2):

    concat = str1 + str2

    letter_dict = {}

    for char in concat:
        letter_dict[char] = letter_dict.get(char, 0) + 1

    values = letter_dict.values()

    odd_count = 0

    for value in values:
        if value % 2 != 0:
            odd_count += 1

    return odd_count <=2



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** All Tests Passed"