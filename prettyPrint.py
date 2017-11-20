def prettyPrint(A):
    n = 2 * A - 1
    matrix = [[0 for x in xrange(n)] for y in xrange(n)]
    for i in xrange(0, n):
        for j in xrange(i, n - i):
            matrix[i][j] = A - i
            matrix[j][i] = A - i
            matrix[n - 1 - i][j] = A - i
            matrix[j][n - 1 - i] = A - i
    for i in xrange(0, n):
        print matrix[i]

A = 4
print (prettyPrint(A))