import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    sx, sy = 0,0
    building = []
    fire = []
    q = []
    visited = [[False] * w for _ in range(h)]

    # 입력
    for i in range(h):
        width = list(input().rstrip())
        building.append(width)
        for j, x in enumerate(width):
            if x == '@':
                sx, sy = i,j
            elif x == '*':
                fire.append((i,j))

    # 불 옮기기
    def move_fire(fire_arr):
        new_fire = []
        for x,y in fire_arr:
            for dx, dy in [[-1, 0], [1, 0], [0, -1],[0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and building[nx][ny] != '#' and building[nx][ny] != '*':
                    building[nx][ny] = '*'
                    new_fire.append((nx, ny))
        return new_fire

    # 이동
    def bfs(queue, fire_arr):
        queue.append((1, sx, sy))
        visited[sx][sy] = True
        while queue:
            fire_arr = move_fire(fire_arr)[:]
            new_queue = []
            for d, x, y in queue:
                if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                    return d
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and building[nx][ny] == '.':
                        new_queue.append((d+1, nx, ny))
                        visited[nx][ny] = True
            queue = new_queue[:]
        return 0

    answer = bfs(q, fire)
    if answer == 0:
        print("IMPOSSIBLE")
    else:
        print(answer)