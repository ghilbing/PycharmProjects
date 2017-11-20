def printNGE(A):
    for i in range(0, len(A), 1):

        next = -1
        for j in range(i + 1, len(A), 1):
            if A[i] < A[j]:
                next = A[j]
                break

        print(str(next))


A = [1,4,6,7,8,4,5,6,7,0,8]
printNGE(A)