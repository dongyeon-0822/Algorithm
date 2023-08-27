from collections import deque

def solution(board):
    answer = -1
    r, g = [], []
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if x == 'R': r = [i, j]
            elif x == 'G': g = [i, j]

    visited = [[False] * len(board[0]) for _ in range(len(board))]
    direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = deque()
    q.append((0, r[0], r[1]))
    visited[r[0]][r[1]] = True
    while q:
        d, x, y = q.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            while 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != 'D':
                nx += dx
                ny += dy
            if [nx-dx, ny-dy] == g:
                return d+1
            if not visited[nx-dx][ny-dy]:
                visited[nx-dx][ny-dy] = True
                q.append((d+1, nx-dx, ny-dy))

    return answer

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))