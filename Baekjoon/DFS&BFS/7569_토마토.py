import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
answer = 0
less_tomato = 0
tomato_loc = []
for h in range(H):
    box = []
    for n in range(N):
        row = list(map(int, input().split()))
        for m, x in enumerate(row):
            if x == 0: less_tomato += 1
            if x == 1: tomato_loc.append((h,n,m))
        box.append(row)
    tomato.append(box)
# 0이 없다면 모두 익음
while less_tomato:
    new_tomato_loc = []
    for z, x, y in tomato_loc:
        for dz, dx, dy in [[0,0,1], [0,0,-1], [0,1,0], [0,-1,0], [1,0,0], [-1,0,0]]:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = 1
                new_tomato_loc.append((nz, nx, ny))
                less_tomato -= 1
    if len(new_tomato_loc) == 0:
        answer = -1
        break
    tomato_loc = new_tomato_loc
    answer += 1

print(answer)
