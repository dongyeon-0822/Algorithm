import sys
input = sys.stdin.readline

mate = {')': '(', ']': '['}
score = {'(': 2, '[': 3}

S = input().rstrip()
answer = []
stack = []
for s in S:
    if not stack: # 비어 있다면 넣기
        stack.append(s)
    elif (s == ')' or s == ']') and mate[s] == stack[-1]:  # 짝이 맞다면 계산
        v = stack.pop()
        if not answer: # 답이 비어있다면
            answer.append([len(stack), score[v]])
        elif answer[-1][0] < len(stack):
            answer.append([len(stack), score[v]])
        elif answer[-1][0] > len(stack):
            depth, value = answer.pop()
            buffer = [len(stack), value * score[v]]
            if answer and answer[-1][0] == buffer[0]:
                depth, value = answer.pop()
                buffer[1] += value
            answer.append(buffer)
        else:
            depth, value = answer.pop()
            answer.append([depth, value + score[v]])
    else: # 짝이 안 맞다면 넣기
        stack.append(s)
if stack:
    print(0)
else:
    print(answer[0][1])