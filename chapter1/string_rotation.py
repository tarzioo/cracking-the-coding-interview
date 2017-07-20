#########################
#Cracking the Coding Interview
#Page 91
#Question 1.9
###############################


"""Assume you have a method, is_substring which checks if one word is a is_substring
   of another. given two strings, check if the first is a rotation of the second string
    
    >>> string_rotation("waterbottle", "erbottlewat")
    True

    >>> string_rotation("foo", "bar")
    False

    >>> string_rotation("foo", "foofoo")
    False

"""

def is_substring(string, sub):
    return string.find(sub) != -1

def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1+s1, s2)
    return False

    




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** All Tests Passed"