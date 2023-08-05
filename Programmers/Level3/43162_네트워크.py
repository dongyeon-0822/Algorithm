def dfs(v, graph, visited):
    if visited[v]: return False

    visited[v] = True
    for i, connect in enumerate(graph[v]):
        if connect:
            dfs(i, graph, visited)
    return True


def solution(n, computers):
    answer = 0

    visited = [False] * n
    for i in range(n):
        if dfs(i, computers, visited):
            answer += 1

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))