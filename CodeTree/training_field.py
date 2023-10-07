import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2**n)]
levels = list(map(int, input().split()))
directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for l in levels:
    # 회전
    if l: # 0이 아닐 때
        new_ice = [[0] * 2**n for _ in range(2**n)]
        for sx in range(0, 2**n, 2**l):
            for sy in range(0, 2**n, 2**l):
                # 부분 격자 선택
                tmp_ice = []
                for i in range(sx, sx + 2**l):
                    row = ice[i][sy:sy + 2**l]
                    tmp_ice.append(row)
                # 4 등분
                divided_tmp_ice = []
                for i in [sx, sx + 2 ** (l-1)]:
                    for j in [sy, sy + 2 ** (l-1)]:
                        block = []
                        for x in range(i, i + 2**(l-1)):
                            row = ice[x][j:j + 2**(l-1)]
                            block.append(row)
                        divided_tmp_ice.append(block)

                # 회전 후 대입
                rotate = [2,0,3,1]
                r = 0
                for i in [sx, sx + 2 ** (l - 1)]:
                    for j in [sy, sy + 2 ** (l - 1)]:
                        for x in range(i, i + 2 ** (l - 1)):
                            for y in range(j, j + 2 ** (l - 1)):
                                new_ice[x][y] = divided_tmp_ice[rotate[r]][x - i][y - j]
                        r += 1
        ice = [row[:] for row in new_ice]
    # 빙하 녹기
    new_ice = [[0] * 2 ** n for _ in range(2 ** n)]
    for x in range(2**n):
        for y in range(2**n):
            cnt = 0
            if ice[x][y] <= 0: continue
            for dx, dy in directs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 2**n and 0 <= ny < 2**n and ice[nx][ny] > 0:
                    cnt += 1
            if cnt >= 3:
                new_ice[x][y] = ice[x][y]
            else:
                new_ice[x][y] = ice[x][y] - 1
    ice = [row[:] for row in new_ice]

# 빙하 세기
visited = [[False] * 2**n for _ in range(2**n)]
count = 0
for i in range(2**n):
    for j in range(2**n):
        if ice[i][j] > 0 and not visited[i][j]:
            q = deque()
            c = 1
            q.append([i, j])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                for dx, dy in directs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 2**n and 0 <= ny < 2**n and ice[nx][ny] > 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([nx, ny])
                        c += 1
            count = max(c, count)

# 빙하의 총 양
print(sum([sum(i) for i in ice]))
# 가장 큰 크기의 얼음 군집
print(count)

