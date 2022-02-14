import sys
input = sys.stdin.readline

N = int(input())
str = []
for i in range(N):
    str.append(input().strip())
for i in str:
    stack = []
    for j in i:
        if len(stack) == 0:
            stack.append(j)
        else:
            if stack[-1] == '(' and j == ')':
                stack.pop(-1)
            else:
                stack.append(j)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')