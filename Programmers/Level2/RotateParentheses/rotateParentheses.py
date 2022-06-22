def isCorrect(str):
    stack = []
    for i in str:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1]=='(' and i==')':
                stack.pop(-1)
            elif stack[-1]=='{' and i=='}':
                stack.pop(-1)
            elif stack[-1] == '[' and i == ']':
                stack.pop(-1)
            else:
                stack.append(i)
    if len(stack)==0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    if len(s)%2 == 1:
        return 0
    for i in range(len(s)):
        if isCorrect(s):
            answer += 1
        s = s[1:]+s[0]

    return answer

solution("[](){}")