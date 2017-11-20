def numRange(A, B, C):
    i = 0
    j = 0
    sum = 0
    count = 0

    while i < len(A):
        sum = sum + A[j]
        if (sum >= B) and (sum <= C):
            count +=1
            j +=1
        elif sum < B:
            j +=1
        elif sum > C:
            i +=1
            j = i
            sum = 0
        if j == len(A):
            sum = 0
            i += 1
            j = i

    print count

A = [10, 5, 1, 0, 2, 1, 2, 4]

B = 6

C = 8

print numRange(A, B, C)