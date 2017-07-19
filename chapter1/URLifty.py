##########################
#Cracking the Coding Interview
#Page 90
#Question 1.3
###############################


"""Write a method to place all spaces in a string with %20.
    
    >>> urlify("Mr John Smith   ", 13)
    'Mr%20John%20Smith'

"""

def urlify(str, num):

    str = str[:num]

    return str.replace(' ', '%20')






if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** All Tests Passed"