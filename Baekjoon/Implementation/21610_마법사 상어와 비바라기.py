import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(M)]
directs = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

clouds = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]
for d, s in command:
    not_clouds = []
    # 구름 이동 및 비 내리기
    for x, y in clouds:
        nx, ny = x + directs[d-1][0] * s, y + directs[d-1][1] * s
        if nx < 0:
            nx = N - (N if abs(nx) % N == 0 else abs(nx) % N)
        if ny < 0:
            ny = N - (N if abs(ny) % N == 0 else abs(ny) % N)
        nx %= N
        ny %= N
        A[nx][ny] += 1
        not_clouds.append((nx, ny))
    # 물복사 마법
    for x, y in not_clouds:
        cnt = 0
        for dx, dy in [(-1,-1), (-1,1), (1,1), (1,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                cnt += 1
        A[x][y] += cnt
    # 2 이상 구름 처리
    new_clouds = [(i, j) for i in range(N) for j in range(N) if A[i][j] >= 2]
    new_clouds = list(set(new_clouds) - set(not_clouds))
    for x, y in new_clouds:
        A[x][y] -= 2
    clouds = new_clouds[:]

answer = sum([sum(row) for row in A])
print(answer)
