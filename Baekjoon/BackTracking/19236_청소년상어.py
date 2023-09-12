import sys
input = sys.stdin.readline

fishes = [[] for _ in range(4)]
for i in range(4):
    row = list(map(int, input().split()))
    for idx in range(0,8,2):
        size, direct = row[idx:idx+2]
        fishes[i].append([size, direct])
directs = [[0, 0], [-1, 0], [-1, -1], [0,-1], [1, -1], [1, 0], [1,1], [0, 1], [-1, 1]]
answers = []

def move_fishes(arr):
    tmp_arr = []
    for line in arr:
        tmp_line = [fish[:] for fish in line]
        tmp_arr.append(tmp_line)

    fishes_dic = {}
    for i in range(4):
        for j in range(4):
            s, d = tmp_arr[i][j]
            fishes_dic[s] = [i, j, d]

    for n in range(1, 17):
        if n not in fishes_dic: continue
        fx, fy, fd = fishes_dic[n]
        dx, dy = directs[fd]
        nfx, nfy = fx + dx, fy + dy
        while not 0 <= nfx < 4 or not 0 <= nfy < 4 or tmp_arr[nfx][nfy] == [-1,-1]:
            fd = 1 if fd + 1 == 9 else fd + 1
            dx, dy = directs[fd]
            nfx, nfy = fx + dx, fy + dy

        # 물고기 바꾸기
        tmp_s, tmp_d = tmp_arr[nfx][nfy]
        tmp_arr[nfx][nfy][0], tmp_arr[nfx][nfy][1] = n, fd
        tmp_arr[fx][fy][0], tmp_arr[fx][fy][1] = tmp_s, tmp_d
        # fishes_dic 바꾸기
        fishes_dic[n] = [nfx, nfy, fd]
        fishes_dic[tmp_s] = [fx, fy, tmp_d]

    return tmp_arr

def dfs(shark_state, arr):
    # 물고기 이동
    move_arr = move_fishes(arr)

    # 상어가 이동할 수 있는 칸 구하기
    eatable = []
    sx, sy, shark_direct, shark_eat = shark_state
    dx, dy = directs[shark_direct]
    nsx, nsy = sx + dx, sy + dy
    while 0 <= nsx < 4 and 0 <= nsy < 4:
        if move_arr[nsx][nsy] != [0, 0]:
            eatable.append([nsx, nsy])
        nsx += dx
        nsy += dy

    if not eatable: # 이동할 수 있는 칸이 없다면 종료
        answers.append(shark_eat)
        return
    for nfx, nfy in eatable: # 이동할 수 있는 물고기 먹기
        fish_size, fish_direct = move_arr[nfx][nfy]
        move_arr[nfx][nfy] = [-1, -1] # 상어 물고기 칸으로 이동
        move_arr[sx][sy] = [0, 0] # 상어 자리는 빈칸
        dfs([nfx, nfy, fish_direct, shark_eat + fish_size], move_arr)
        move_arr[nfx][nfy] = [fish_size, fish_direct]
        move_arr[sx][sy] = [-1, -1]

s, d = fishes[0][0]
fishes[0][0] = [-1, -1] # 상어가 있는 자리
shark = [0, 0, d, s] # [x, y, direct, eat]
dfs(shark, fishes)
print(max(answers))