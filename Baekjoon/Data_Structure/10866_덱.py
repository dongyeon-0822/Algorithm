import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == "pop_front":
            if not q:
                print(-1)
            else:
                print(q.popleft())
        elif cmd[0] == "pop_back":
            if not q:
                print(-1)
            else:
                print(q.pop())
        elif cmd[0] == "size":
            print(len(q))
        elif cmd[0] == "empty":
            if not q:
                print(1)
            else:
                print(0)
        elif cmd[0] == "front":
            if not q:
                print(-1)
            else:
                print(q[0])
        else: # back
            if not q:
                print(-1)
            else:
                print(q[-1])
    else:
        if cmd[0] == "push_front":
            q.appendleft(cmd[1])
        else: # push_back
            q.append(cmd[1])
