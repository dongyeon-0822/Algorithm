import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
cost = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())

def dijkstra(s):
    q = []
    cost[s] = 0
    heapq.heappush(q,(0,s))
    while q:
        now_cost, now_city = heapq.heappop(q)
        if now_cost > cost[now_city]:
            continue
        for bus in graph[now_city]:
            sum_cost = cost[now_city] + bus[1]
            if sum_cost < cost[bus[0]]:
                cost[bus[0]] = sum_cost
                heapq.heappush(q, (sum_cost, bus[0]))

dijkstra(start)

print(cost[end])