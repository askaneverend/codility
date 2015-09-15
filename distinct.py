def solution(A):
    # write your code in Python 2.7
    A.sort()
    n = len(A)
    if n == 0:
        return 0
    disn = 1
    for i in xrange(1,n):
        if(A[i] != A[i - 1]):
            disn += 1
    return disn