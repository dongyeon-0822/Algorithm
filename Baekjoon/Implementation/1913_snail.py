import sys
input = sys.stdin.readline

N = int(input())
n = int(input())
x, y = 0, 0

arr = [[0]*N for _ in range(N)]
turn = []
for i in range(N, 0, -1):
    if i != N:
        turn.append(i)
    turn.append(i)
count = N*N
i = -1
j = 0
flag = 1
t = 0
while count:
    if flag % 4 == 1:
        i += 1
    elif flag % 4 == 2:
        j += 1
    elif flag % 4 == 3:
        i -= 1
    elif flag % 4 == 0:
        j -= 1
    arr[i][j] = count
    turn[t] -= 1
    if count == n:
        x, y = i+1, j+1
    if turn[t] == 0:
        flag += 1
        t += 1
    count -= 1
for i in arr:
    print(*i, sep=' ')
print(x, y)