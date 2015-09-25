def solution(S):
    # write your code in Python 2.7
    stack = []
    for i in xrange(len(S)):
        if S[i] == "{" or S[i] == "(" or S[i] == "[" :
            stack.append(S[i])
        elif (S[i] == "}" or S[i] == ")" or S[i] == "]") and len(stack) == 0:
            return 0
        elif S[i] == "}" and len(stack) != 0 and stack[-1] != "{":
            return 0
        elif S[i] == "}" and len(stack) != 0 and stack[-1] == "{":
            stack.pop()
        elif S[i] == ")" and len(stack) != 0 and stack[-1] != "(":
            return 0
        elif S[i] == ")" and len(stack) != 0 and stack[-1] == "(":
            stack.pop()
        elif S[i] == "]" and len(stack) != 0 and stack[-1] != "[":
            return 0
        elif S[i] == "]" and len(stack) != 0 and stack[-1] == "[":
            stack.pop()
    if len(stack) != 0:
        return 0
    else:
        return 1

def solution(S):
    stack = []
    braces = {"{":"}", "(":")", "[":"]"}
    for c in S:
        if c in braces:
            stack.append(c)
        elif stack and bracks[stack[-1]] == c:
            stack.pop()
        else:
            return False
    return not stack

if __name__  == "__main__":
#    S =  ")("
#    S = 10K+1 ('s followed by 10K )'s + )( + ()
    S = 10001 * "(" + 10000 * ")" + ")(()"
    print solution(S)