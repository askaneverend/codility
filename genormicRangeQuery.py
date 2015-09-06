def prefix_sum(A):
    n = len(A)
    P = [0] * (n + 1)
    for i in xrange(1,n):
        P[i] = P[0] + A[i]
    return P

def count_total(A,x,y):
    return P[y + 1] - P[x]

def solution(S, P, Q):
    # write your code in Python 2.7
    n = len(S)
    CA = [0] * (n + 1)
    CC = [0] * (n + 1)
    CG = [0] * (n + 1)
    CT = [0] * (n + 1)
    nA=nC=nG=nT = 0
    count = [CA, CC, CG, CT]
    for i in xrange(n):
        if(S[i] == "A"):
            nA += 1
            CA[i + 1] = nA 
            CC[i + 1] = nC
            CG[i + 1] = nG
            CT[i + 1] = nT
        if(S[i] == "C"):
            nC += 1
            CA[i + 1] = nA 
            CC[i + 1] = nC
            CG[i + 1] = nG
            CT[i + 1] = nT            
        if(S[i] == "G"):
            nG += 1
            CA[i + 1] = nA 
            CC[i + 1] = nC
            CG[i + 1] = nG
            CT[i + 1] = nT 
        if(S[i] == "T"):
            nT += 1
            CA[i + 1] = nA 
            CC[i + 1] = nC
            CG[i + 1] = nG
            CT[i + 1] = nT 
    m = len(P)
    Query = [0] * m
    for i in range(m):
        for j in range(4):
            if(count[j][Q[i] + 1] > count[j][P[i]]):
                Query[i] = j + 1
                break
    return Query

if __name__ == "__main__":
    S = "CAGCCTA"
    P = [2,5,0]
    Q = [4,5,6]
    print solution(S,P,Q)


    