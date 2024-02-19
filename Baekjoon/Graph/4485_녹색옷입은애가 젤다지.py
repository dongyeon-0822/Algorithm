import sys
import heapq
input = sys.stdin.readline

cnt = 0
while True:
    N = int(input())
    if N == 0: break
    cnt += 1
    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[int(1e9)] * N for _ in range(N)]

    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
    distance[0][0] = board[0][0]
    while q:
        d, x, y = heapq.heappop(q)
        for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and d + board[nx][ny] < distance[nx][ny]:
                distance[nx][ny] = d + board[nx][ny]
                heapq.heappush(q, (d + board[nx][ny], nx, ny))

    print("Problem " + str(cnt) + ": " + str(distance[N-1][N-1]))