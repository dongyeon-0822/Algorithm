def dfs(v):
    global visited
    global graph
    global cnt
    visited[v] = True
    cnt += 1
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

def solution(n, wires):
    global visited
    global graph
    global cnt
    answer = []
    for i in range(n-1):
        visited = [False] * (n+1)
        graph = [[] for _ in range(n+1)]
        for j in range(n-1): # 그래프 생성
            if i != j:
                a,b = wires[j]
                graph[a].append(b)
                graph[b].append(a)
        cnt = 0
        dfs(1)
        result = abs((n - 2*cnt))
        if result <= 1:
            return result
        answer.append(result)
    return min(answer)

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))