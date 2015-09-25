def solution(A, B):
    # write your code in Python 2.7
    fish = []
    for i in xrange(len(A)):
        if len(fish) == 0 or B[i] == 1:
            fish.append((A[i], B[i]))
        elif B[i] == 0 and fish[-1][1] == 0:
            fish.append((A[i], B[i]))
        elif B[i] == 0:
            j = len(fish) - 1
            while j >= 1:
                if fish[j][1] == 1 and fish[j][0] < A[i]:
                    fish.pop()
                    j -= 1
                else:
                    break;
            else:
                fish.append((A[i], B[i]))
        print fish
            
    return len(fish)

def solution2(A, B):
    # write your code in Python 2.7
    fish = []
    for i in xrange(len(A)):
        if len(fish) == 0 or B[i] == 1:
            fish.append((A[i], B[i]))
        elif B[i] == 0 and fish[-1][1] == 0:
            fish.append((A[i], B[i]))
        else:
            while len(fish) >= 1 and fish[-1][1] == 1:
                if fish[-1][0] < A[i]:
                    fish.pop()
                else:
                    break;
            else:
                fish.append((A[i], B[i]))
            
    return len(fish)

def sulution3(A, B):
    alive_num = 0
    downStack = []
    for i in xrange(len(A)):
        if B[i] == 1:
            downStack.append(A[i])
        else:
            while(len(downStack) >= 1):
                if downStack[-1] < A[i]:
                    downStack.pop()
                else:
                    break;
            else:
                alive_num += 1
    return alive_num + len(downStack)

if __name__ == "__main__":
    A = [4,3,2,1,5]
    B = [0,1,0,0,0]
    print solution2(A, B)