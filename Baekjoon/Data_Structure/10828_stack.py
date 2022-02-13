import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        arr.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(-1))
    elif cmd[0] == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif cmd[0] == 'size':
        print(len(arr))
    elif cmd[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)