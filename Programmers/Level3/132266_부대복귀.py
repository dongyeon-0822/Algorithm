from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)

    distance = [int(1e9) for _ in range(n+1)]
    q = deque()
    visited = [False] * (n+1)

    q.append((0, destination))
    visited[destination] = True
    distance[destination] = 0
    while q:
        d, node = q.popleft()
        for n_node in graph[node]:
            if visited[n_node]: continue
            q.append((d + 1, n_node))
            visited[n_node] = True
            distance[n_node] = d + 1
    for s in sources:
        result = distance[s] if distance[s] != int(1e9) else -1
        answer.append(result)
    return answer

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))