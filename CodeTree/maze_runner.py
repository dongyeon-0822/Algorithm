import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
members = [list(map(int, input().split())) for _ in range(M)]
ex, ey = map(int, input().split())
directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
distance = 0

while K:
    # 모든 참가자 이동
    next_members = []
    for mx, my in members:
        moves = []
        min_distance = abs(mx - ex) + abs(my - ey)
        flag = False
        for dx, dy in directs:
            nx, ny = mx + dx, my + dy
            if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] == 0:
                if nx == ex and ny == ey: # exit
                    distance += 1
                    flag = True
                    break
                n_min_distance = abs(nx - ex) + abs(ny - ey)
                if n_min_distance < min_distance:
                    moves.append([nx, ny])
        if not flag:
            if len(moves) == 0:
                next_members.append([mx, my])
            elif len(moves) == 1:
                next_members.append(moves[0])
                distance += 1
            elif len(moves) == 2:
                for nx, ny in moves:
                    if nx != mx:
                        next_members.append([nx, ny])
                        distance += 1
                        break
    members = [m[:] for m in next_members]
    if not members: break
    # 사각형 찾기
    squares = []
    for mx, my in members:
        side = max(abs(mx - ex), abs(my - ey))
        sx = 1 if max(mx, ex) - side < 1 else max(mx, ex) - side
        sy = 1 if max(my, ey) - side < 1 else max(my, ey) - side
        squares.append([side, sx, sy])
    squares.sort()
    # 사각형 회전 - 시계 90도
    side, sx, sy = squares[0]
    square = []
    for x in range(sx, sx + side + 1):
        row = []
        for y in range(sy, sy + side + 1):
            n = board[x][y]
            nn = 0
            if n == 0:
                if [x,y] in members:
                    for _ in range(members.count([x,y])):
                        nn += -1
                        members.remove([x,y])
                elif x == ex and y == ey:
                    nn = -11
                else: nn = n
            else: nn = n - 1
            row.append(nn)
        square.append(row)
    square = list(map(list, zip(*square[::-1])))

    for i in range(sx, sx + side + 1):
        for j in range(sy, sy + side + 1):
            x, y = i - sx, j - sy
            if -11 < square[x][y] < 0: # member
                for _ in range(abs(square[x][y])):
                    members.append([i,j])
                    board[i][j] = 0
            elif square[x][y] == -11: # exit
                ex, ey = i, j
                board[i][j] = 0
            else:
                board[i][j] = square[x][y]
    K -= 1

print(distance)
print(ex, ey)