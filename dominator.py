def solution(A):
    if not A:
        return -1
    num = 0
    k = A[0]
    for n in A:
        num += 1 if n == k else -1
        if num == 0:
            k = n
            num += 1
    num = 0
    dominator = -1
    for i in xrange(len(A)):
        if A[i] == k:
            dominator = i
            num += 1
    if (float(num) / len(A)) <= 0.5:
        return -1
    else:
        return dominator


if __name__ == "__main__":
    A = [0,0,1,1,1] 
    print solution(A)
