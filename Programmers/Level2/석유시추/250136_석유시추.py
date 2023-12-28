import sys
sys.setrecursionlimit(10**8)

def solution(land):
    def dfs(x, y, cnt, col):
        visited[x][y] = True
        cnt += 1
        col.append(y)
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] and not visited[nx][ny]:
                cnt, col = dfs(nx, ny, cnt, col)
        return cnt, col

    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    answer = [0] * m
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 or visited[i][j]: continue
            count, columns = dfs(i, j, 0, [])
            for c in set(columns):
                answer[c] += count
    return max(answer)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))