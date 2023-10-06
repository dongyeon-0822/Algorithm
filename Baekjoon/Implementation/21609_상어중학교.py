import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directs = [[-1,0], [1,0], [0,-1], [0, 1]]

def bfs(x, y, visit, arr):
    # 무지개 블록 방문 가능 처리
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: visit[i][j] = False

    size, rainbow_size, min_x, min_y, color = 0, 0, x, y, arr[x][y]
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    while q:
        x, y = q.popleft()
        if arr[x][y] == 0:
            size += 1
            rainbow_size += 1
        else:
            size += 1
        for dx, dy in directs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > -1 and not visit[nx][ny]:
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = True
                elif arr[nx][ny] == color:
                    q.append((nx, ny))
                    visit[nx][ny] = True
    return [size, rainbow_size, min_x, min_y, color]

def gravity():
    # 중력 작용
    board_col = list(map(list, zip(*board)))
    new_board = []
    for col in board_col:
        nums, blanks = [], []
        i = N - 1
        while i >= 0:
            if col[i] != -1:
                if col[i] != -2:
                    nums.append(col[i])
                else:
                    blanks.append(col[i])
            else:
                for idx in range(i + 1, i + 1 + len(nums) + len(blanks)):
                    if blanks:
                        col[idx] = blanks.pop()
                    else:
                        col[idx] = nums.pop()
                nums, blanks = [], []
            i -= 1
        else:
            for idx in range(len(nums) + len(blanks)):
                if blanks:
                    col[idx] = blanks.pop()
                else:
                    col[idx] = nums.pop()
        new_board.append(col)
    return list(map(list, zip(*new_board)))

score = 0
while True:
    # 블록 개수 찾기 (bfs)
    visited = [[False] * N for _ in range(N)]
    blocks = [] # [블록의 크기, 무지개 블록의 색, x, y, 블록의 색]
    for i in range(N):
        for j in range(N):
            if board[i][j] > -1 and board[i][j] != 0 and not visited[i][j]:
                block = bfs(i, j, visited, board)
                if block[0] >= 2:
                    blocks.append(block)

    if not blocks: break # 블록이 없다면
    blocks.sort(reverse=True) # 블록이 있다면
    # 블록 지우기
    x, y, color = blocks[0][2], blocks[0][3], blocks[0][4]
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append((x,y))
    visited[x][y] = True
    board[x][y] = -2
    while q:
        x, y = q.popleft()
        for dx, dy in directs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and (board[nx][ny] == 0 or board[nx][ny] == color):
                q.append((nx,ny))
                visited[nx][ny] = True
                board[nx][ny] = -2
    # 점수 획득
    score += blocks[0][0]**2
    # 중력 작용
    new_board = gravity()
    # 반시계 90도 회전
    board = list(map(list, zip(*new_board)))[::-1]
    # 중력 작용
    new_board = gravity()
    board = [row[:] for row in new_board]


print(score)
