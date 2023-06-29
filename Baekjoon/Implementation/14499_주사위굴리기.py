from collections import deque
import sys
input = sys.stdin.readline

def roll_dice(d, direct):
    horizontal = deque([d['w'], d['b'], d['e'], d['t']])
    vertical = deque([d['n'], d['b'], d['s'], d['t']])

    if direct == 1:
        horizontal.rotate(-1)
        d['w'], d['b'], d['e'], d['t'] = list(horizontal)
    elif direct == 2:
        horizontal.rotate(1)
        d['w'], d['b'], d['e'], d['t'] = list(horizontal)
    elif direct == 3:
        vertical.rotate(1)
        d['n'], d['b'], d['s'], d['t'] = list(vertical)
    elif direct == 4:
        vertical.rotate(-1)
        d['n'], d['b'], d['s'], d['t'] = list(vertical)
    return d

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = {'b': 0, 't': 0, 'e': 0, 'w': 0, 'n': 0, 's': 0}

for command in commands:
    nx = x + dx[command-1]
    ny = y + dy[command-1]
    if 0 <= nx < N and 0 <= ny < M:
        dice = roll_dice(dice, command)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice['b']
        else:
            dice['b'] = graph[nx][ny]
            graph[nx][ny] = 0
        print(dice['t'])
        x, y = nx, ny
