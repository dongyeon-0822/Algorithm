import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    distance_tmp = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append(start)
    distance_tmp[start[0]][start[1]] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or distance_tmp[nx][ny] != 0 or graph_tmp[nx][ny] == 1:
                continue
            if graph_tmp[nx][ny] == 0:
                distance_tmp[nx][ny] = distance_tmp[x][y] + 1
                queue.append((nx,ny))
            elif graph_tmp[nx][ny] == 2:
                return distance_tmp[x][y]

N, M = map(int, input().split())
graph = []
chickens = []
answer = []
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j, x in enumerate(tmp):
        if x == 2: # 치킨집이라면 좌표값 저장
            chickens.append((i,j))

# m개 선택한 치킨집만 존재하도록 graph 설정
graph_tmp = []
distance_tmp = []
for chicken in list(combinations(chickens, len(chickens)-M)):
    graph_tmp = [x[:] for x in graph]
    for i,j in chicken:
        graph_tmp[i][j] = 0
    # 집이면 치킨 거리까지 최단거리를 각각 구하여 더한다.
    chicken_distance = 0
    for i in range(N):
        for j in range(N):
            if graph_tmp[i][j] == 1:
                chicken_distance += bfs((i,j))
    answer.append(chicken_distance)

print(min(answer))