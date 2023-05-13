import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

tomatoes = [(i,j) for j in range(M) for i in range(N) if arr[i][j] == 1]

if len(tomatoes) == M*N:
    print(0)
else:
    days = 0
    while len(tomatoes) != 0:
        new_tomatoes = []
        for x,y in tomatoes:
            for direct in range(4):
                nx = x + dx[direct]
                ny = y + dy[direct]
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    new_tomatoes.append((nx,ny))
        tomatoes = new_tomatoes
        days += 1
    tomatoes = [(i, j) for j in range(M) for i in range(N) if arr[i][j] == 0]
    if len(tomatoes) != 0:
        print(-1)
    else:
        print(days-1)
