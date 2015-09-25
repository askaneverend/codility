def solution(A):
    candidate = A[0]
    num = 0
    for element in A:
        num += 1 if element == candidate else -1
        if num == 0:
            candidate = element
            num += 1
    num_candidate = 0
    for element in A:
        if element == candidate:
            num_candidate += 1
    if num_candidate <= len(A)/2:
        return 0
    else:
        leader = candidate
    num_current_candidate = 0
    equil_leader = 0
    for i in xrange(len(A)):
        if A[i] == leader:
            num_current_candidate += 1
        if num_current_candidate > (i + 1)/2 and (num_candidate - num_current_candidate) > (len(A) - i - 1)/2:
            equil_leader += 1
    return equil_leader
    

if __name__ == "__main__":
    A = [4, 3, 4, 4, 4, 2] 
    print solution(A)
#    print getLead(A[:3])
#    print getLeadIndex(A[3:])
