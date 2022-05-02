# 정보 입력받기
N, M = map(int, input().split())
A, B, direct = list(map(int, input().split()))
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]
visited[A][B] = 1
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_left():
    global direct
    direct -= 1
    if direct < 0:
        direct = 3

count = 1
turns = 0
while True:
    turn_left()
    a = A + move[direct][0]
    b = B + move[direct][1]
    if 0 <= a < N and 0 <= b < M and visited[a][b] == 0 and maps[a][b] == 0:
        A = a
        B = b
        visited[a][b] = 1
        count += 1
        turns = 0
        continue
    else:
        turns += 1
    if turns == 4: # 다시 원래 방향
        a = A - move[direct][0]
        b = B - move[direct][0]
        if maps[a][b] == 0:
            A = a
            B = b
            turns = 0
        else:
            break
print(count)


