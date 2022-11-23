import heapq

def solution(N, road, K):
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    for a,b,c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n,d in graph[node]:
            cost = d + dist
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))

    answer = 0
    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1
    return answer

solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)