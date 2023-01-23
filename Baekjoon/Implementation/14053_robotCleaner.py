import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y, direct = r, c, d
while True:
    if graph[x][y] == 0:
        graph[x][y] = 2 # 현재 위치 청소
        answer += 1

    flag = False # 네 방향 모두 청소 가능
    for _ in range(4): # 왼쪽 방향 부터 탐색 진행
        direct = direct-1 if direct != 0 else 3 # 현재 방향의 왼쪽
        n_x = x + dx[direct]
        n_y = y + dy[direct]
        if 0 < n_x < N-1 and 0 < n_y < M-1 and graph[n_x][n_y] == 0: # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
            x, y = n_x, n_y
            flag = True
            break
    flag2 = False # 후진 가능 한지
    if not flag: # 네 방향 모두 청소가 이미 되어있거나 벽인 경우, 후진
        n_x = x - dx[direct]
        n_y = y - dy[direct]
        if 0 < n_x < N - 1 and 0 < n_y < M - 1 and graph[n_x][n_y] == 2:
            x, y = n_x, n_y
            flag2 = True
            continue
    if not flag and not flag2:
        break

print(answer)