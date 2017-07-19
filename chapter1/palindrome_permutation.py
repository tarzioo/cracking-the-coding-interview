##########################
#Cracking the Coding Interview
#Page 91
#Question 1.4
###############################


"""Given a string, write a function to check if it is a permutation of a palindrome
    
    >>> is_palindrome("Tact coa")
    True

    >>> is_palindrome("mars")
    False

"""

def is_palindrome(str):

    #strip white spaces, and change to lower

    str = str.replace(" ", "")
    str= str.lower()

    #get letter count
    letter_dict = {}

    for char in str:
        letter_dict[char] = letter_dict.get(char, 0) + 1

    odd_count = 0

    #get values from  letter count. correct answer can only allow for 1 or 0 odd values
    value = letter_dict.values()

    for item in value:
        if item % 2 != 0:
            odd_count += 1

    return odd_count <= 1








if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** All Tests Passed"