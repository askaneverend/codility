def solution(S):
    # write your code in Python 2.7
    num = 0
    for i in xrange(len(S)):
        if S[i] == '(':
            num += 1
        elif S[i] == ')':
            num -= 1
        if num < 0:
            return 0
    if num == 0:
        return 1
    else:
        return 0