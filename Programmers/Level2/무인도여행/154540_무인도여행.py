import sys
sys.setrecursionlimit(50000000)
visited = [[False] * 100 for _ in range(100)]

def dfs(x, y, maps):
    if x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0]) or maps[x][y] == 'X':
        return 0
    if not visited[x][y]:
        visited[x][y] = True
        return int(maps[x][y]) + dfs(x - 1, y, maps) + dfs(x + 1, y, maps) + dfs(x, y - 1, maps) + dfs(x, y + 1, maps)
    return 0

def solution(maps):
    answer = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            food = dfs(i, j, maps)
            if food != 0:
                answer.append(food)

    if len(answer) == 0: return [-1]
    else : return sorted(answer)
