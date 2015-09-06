def prefix_sum(A):
    n = len(A)
    P = [0] * (n + 1)
    for i in xrange(1,n):
        P[i] = P[0] + A[i]
    return P

def count_total(A,x,y):
    return P[y + 1] - P[x]

def solution(A):
    # write your code in Python 2.7
    minAvg = (A[0] + A[1])/2.0
    minPoi = 0
    n = len(A)
    for i in xrange(0, n-2):
        if (A[i] + A[i + 1])/2.0 < minAvg:
            minAvg = (A[i] + A[i + 1])/2.0
            minPoi = i
        if (A[i] + A[i + 1] + A[i + 2])/3.0 < minAvg:
            minAvg = (A[i] + A[i + 1] + A[i + 2])/3.0
            minPoi = i
    if (A[n - 1] + A[n - 2])/2.0 < minAvg:
            minAvg = (A[n - 1] + A[n - 2])/2.0
            minPoi = n-2
    return minPoi