def solution(N, A):
    # write your code in Python 2.7
    lenA = len(A)
    count = [0] * N
    maxValue = 0
    adjustValue = 0
    for i in xrange(lenA):
        if(A[i] != (N + 1)):
            if(count[A[i] - 1] < adjustValue) :
                count[A[i] - 1] = adjustValue
            count[A[i] - 1] += 1
            if(count[A[i] -1] > maxValue):
                maxValue = count[A[i] - 1]
        else:
            adjustValue = maxValue
    for j in xrange(N):
        if(count[j] < adjustValue):
            count[j] = adjustValue
    return count