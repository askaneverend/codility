def solution(A):
    # write your code in Python 2.7
    A.sort()
    n = len(A)
    if n<= 2:
        return 0
    for i in xrange(0,(n - 2)):
        if ((A[i] + A[i + 1]) > A[i + 2]) and ((A[i] + A[i + 2]) > A[i + 1]):
            return 1
    return 0