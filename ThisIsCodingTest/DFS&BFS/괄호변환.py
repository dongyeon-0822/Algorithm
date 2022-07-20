# https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3

def is_Correct(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)
    if len(stack) == 0:
        return True
    else:
        return False

def divide(s):
    if len(s) == 0: # 1
        return ""
    cnt_left = 0
    cnt_right = 0
    u = ""
    v = ""
    for i, c in enumerate(s):
        if c == '(':
            cnt_left += 1
        else:
            cnt_right += 1
        if cnt_left == cnt_right:
            u = s[:i + 1] # 2
            v = s[i + 1:] # 2
            if is_Correct(u): # 3
                return u + divide(v)
            else: # 4
                tmp = "("
                tmp += divide(v)
                tmp += ")"
                for t in u[1:-1]:
                    if t == '(':
                        tmp += ")"
                    else:
                        tmp += "("
                return tmp

def solution(p):
    answer = ""
    if len(p) == 0:
        return answer
    if is_Correct(p):
        return p
    return divide(p)

print(solution(")("))