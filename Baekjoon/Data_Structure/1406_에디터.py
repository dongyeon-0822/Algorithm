import sys
input = sys.stdin.readline

S = input().rstrip()
M = int(input())
left, right = list(S), []

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        if not left: continue
        right.append(left.pop())
    elif cmd[0] == 'D':
        if not right: continue
        left.append(right.pop())
    elif cmd[0] == 'B':
        if not left: continue
        left.pop()
    else:
        left.append(cmd[1])
print(''.join(left + right[::-1]))