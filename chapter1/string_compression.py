#########################
#Cracking the Coding Interview
#Page 91
#Question 1.6
###############################


"""Implement a method to preform basic string compression using the count if the repeated characters
    
    >>> string_compression("aabcccccaaa")
    'a2b1c5a3'

    >>> string_compression("abcdefasd")
    'abcdefasd'

"""

def string_compression(s):

    result = []
    count = 0

    for i in range(len(s)):
        if i != 0 and s[i] != s[i-1]:
            result.append(s[i-1] + str(count))
            count = 0

        count += 1

    result.append(s[-1] + str(count))

    return min(s, ''.join(result), key=len)





if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** All Tests Passed"