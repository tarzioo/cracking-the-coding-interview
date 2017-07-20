#########################
#Cracking the Coding Interview
#Page 91
#Question 1.8
###############################


"""write an algorithm such that if an element in MxN matrix is 0, it's entire row and colum are set to zero
    
    >>> zero_matrix([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ])
    [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])


"""

def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = []
    cols = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for row in rows:
        nullify_row(matrix, row)

    for col in cols:
        nullify_col(matrix, col)

    return matrix


    def nullify_row(matrix, row):
        for i in range(len(matric[0])):
            matric[row][i] = 0

    def nullify_col(matrix, col):
        for i in range(len(matrix)):
            matrix[i][col] = 0






if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** All Tests Passed"