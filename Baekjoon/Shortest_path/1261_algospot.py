import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
M, N = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]
distance = [[INF]*M for _ in range(N)]

# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start[0]][start[1]] = 0
    while q:
        dist, [x,y] = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                cost = distance[x][y] + int(graph[nx][ny])
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost, [nx,ny]))

dijkstra([0,0])
print(distance[N-1][M-1])