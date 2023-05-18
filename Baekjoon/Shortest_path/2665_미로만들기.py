import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
graph = [input().rstrip() for _ in range(n)]
distance = [[INF] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start[0]][start[1]] = 0
    while q:
        dist, [x,y] = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == '0':
                    cost = distance[x][y] + 1
                else:
                    cost = distance[x][y]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost,[nx,ny]))

dijkstra([0,0])
print(distance[n-1][n-1])