# https://www.acmicpc.net/board/view/49289 : 반례
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph = [{} for _ in range(V+1)]
visited = [False] * (V+1)
distance = [INF] * (V+1)

for _ in range(E):
    u,v,w = list(map(int,input().split()))
    if v in graph[u]:
        if graph[u][v] > w:
            graph[u][v] = w
    else:
        graph[u][v] = w

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 거리가 가장 짧은 노드 뽑기
        if distance[now] < dist: # 이미 갱신한 거리가 현재 뽑은 노드의 거리보다 작은 경우
            continue
        for a,b in graph[now].items(): # 현재 노드와 인접한 노드 확인
            cost = dist + b
            # 현재 노드를 거쳐 다른 노드로 가는 비용이 더 짧은 경우
            if cost < distance[a]:
                distance[a] = cost
                heapq.heappush(q,(cost, a))

dijkstra(K)

for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])