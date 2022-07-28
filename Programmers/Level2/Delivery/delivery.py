from collections import deque

def solution(N, road, K):
    answer = 1
    graph = [[] for _ in range(N+1)]
    distance = [0] * (N+1)
    for r in road:
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])
    q = deque()
    q.append(1)
    while len(q) != 0:
        node = q.popleft()
        for v, d in graph[node]:
            if not distance[v] or distance[v] > distance[node] + d: # 방문하지 않았거나 더 짧은 경우
                q.append(v)
                distance[v] = distance[node] + d
    for i in range(2,N+1):
        if 0 < distance[i] <= K:
            answer += 1
    return answer

solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)