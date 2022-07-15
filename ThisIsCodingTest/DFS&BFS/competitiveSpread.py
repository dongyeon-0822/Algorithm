import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
tmp = [x[:] for x in arr]

def spread(x,y):
    direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(4):
        dx = x + direct[i][0]
        dy = y + direct[i][1]
        if 0 <= dx < N and 0 <= dy < N and not arr[dx][dy] and (not tmp[dx][dy] or tmp[dx][dy] > arr[x][y]):
            tmp[dx][dy] = arr[x][y]

flag = False
for s in range(S):
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                spread(i, j)
    arr = [x[:] for x in tmp]
    if arr[X - 1][Y - 1]:
        print(arr[X - 1][Y - 1])
        flag = True
        break
if not flag:
    print(arr[X - 1][Y - 1])