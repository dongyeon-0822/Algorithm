from collections import deque

def bfs(maps, x, y, end):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    distance = 0
    found = [0,0]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    q = deque()
    q.append((0, [x, y]))
    visited[x][y] = True
    while q:
        d, [x, y] = q.popleft()
        flag = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                if maps[nx][ny] == end:
                    distance = d + 1
                    found = [nx, ny]
                    flag = True
                    break
                else:
                    visited[nx][ny] = True
                    q.append((d + 1, [nx, ny]))
        if flag: break
    return distance, found

def solution(maps):
    answer = 0

    # 시작 좌표 찾기
    x, y = 0, 0
    for i, m in enumerate(maps):
        if 'S' in m:
            x, y = i, m.index('S')
            break

    # S -> L 까지 최단 거리 찾기
    distanceStoL, [lx, ly] = bfs(maps, x, y, 'L')
    if distanceStoL == 0:
        return -1
    # L -> E 까지 최단 거리 찾기
    distanceLtoE, [ex, ey] = bfs(maps, lx, ly, 'E')
    if distanceLtoE == 0:
        return -1

    answer = distanceStoL + distanceLtoE
    return answer

print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))