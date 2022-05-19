N, M = map(int, input().split())

# map 정보 입력받기
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    # 아직 방문하지 않은 노드라면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)