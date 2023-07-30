import sys
input = sys.stdin.readline

def rotate_array(arr, clean, way):
    if not way: # 반시계
        x1, y1, x2, y2 = 0, 0, clean[0][0], len(arr[0])-1
        tmp_arr = [a[:] for a in arr]
        arr[x1][0:y2] = tmp_arr[x1][1:y2+1]
        for i in range(x1 + 1, x2 + 1):
            arr[i-1][y2] = tmp_arr[i][y2]
        arr[x2][1:y2+1] = tmp_arr[x2][0:y2]
        for i in range(x1, x2):
            arr[i+1][y1] = tmp_arr[i][y1]
        arr[x2][0], arr[x2][1] = -1, 0
    else: # 시계 방향
        x1, y1, x2, y2 = clean[1][0], 0, len(arr) - 1, len(arr[0]) - 1
        tmp_arr = [a[:] for a in arr]
        arr[x1][1:y2+1] = tmp_arr[x1][0:y2]
        for i in range(x1, x2):
            arr[i+1][y2] = tmp_arr[i][y2]
        arr[x2][0:y2] = tmp_arr[x2][1:y2+1]
        for i in range(x1+1, x2+1):
            arr[i-1][y1] = tmp_arr[i][y1]
        arr[x1][0], arr[x1][1] = -1, 0

maps = []
cleaner = []
dusts = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
R, C, T = map(int, input().split())
for r in range(R):
    row = list(map(int, input().split()))
    if row[0] == -1: cleaner.append((r,0))
    for c in range(C):
        if row[c] > 0:
            dusts.append((r,c))
    maps.append(row)

for _ in range(T):
    tmp_maps = [m[:] for m in maps]

    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] >= 5:
                amount = maps[r][c] // 5
                for direct in range(4):
                    nx = r + dx[direct]
                    ny = c + dy[direct]
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in cleaner:
                        tmp_maps[nx][ny] += amount
                        tmp_maps[r][c] -= amount
    maps = [m[:] for m in tmp_maps]
    rotate_array(maps, cleaner, 0)
    rotate_array(maps, cleaner, 1)

print(sum(sum(row) for row in maps) + 2)
