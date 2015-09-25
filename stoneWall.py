def solution(H):
    # write your code in Python 2.7
    n = len(H)
    stoneNum = 0
    stack = [0] * n
    stackNum = -1

    for i in xrange(n):
        while (stack[stackNum] > H[i]) and (stackNum > 0) :
            stackNum -= 1
        if (stackNum == -1) or stack[stackNum] < H[i]:
            stackNum += 1
            stack[stackNum] = H[i]
            stoneNum +=1
    return stoneNum

def solution2(H):
    stoneNum = 0
    stack = []
    for i in xrange(len(H)):
        while(len(stack) != 0 and stack[-1] > H[i]):
            stack.pop()
        if(len(stack) == 0 or stack[-1] < H[i]):
             stack.append(H[i])
             stoneNum += 1
        print stack
    return stoneNum

if __name__ == "__main__":
    H = [8,8,5,7,9,8,7,4,8]
    solution2(H)