# https://www.acmicpc.net/problem/14502
# python3로 제출 시, 시간초과 -> bfs 로 고처야 한다고 한다. (함수호출이 느려서)
# pypy3오 제출 시, 성공!

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = []

def spread_virus(x, y):
    direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(4):
        nx = x + direct[i][0]
        ny = y + direct[i][1]
        if 0 <= nx < N and 0 <= ny < M and not tmp[nx][ny]:
            tmp[nx][ny] = 2
            spread_virus(nx, ny)

def dfs(wall):
    global tmp
    if wall == 3:
        tmp = [x[:] for x in arr]
        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 2:
                    spread_virus(i, j)
        answer.append(sum([x.count(0) for x in tmp]))
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(wall + 1)
                arr[i][j] = 0
dfs(0)
print(max(answer))