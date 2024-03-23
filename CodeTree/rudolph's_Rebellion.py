import sys
input = sys.stdin.readline

N, M, P, C, D = map(int, input().split())
board = [['.'] * (N+1) for _ in range(N+1)]
r_r, r_c = map(int, input().split()) # 루돌프 초기 위치
board[r_r][r_c] = 0 # 루돌프 = 0
santa = [[] for _ in range(P+1)]
for _ in range(P):
    n, s_r, s_c = map(int, input().split())
    santa[n] = [s_r, s_c, False, False, 0, 0] # (r, c, 탈락 여부, 기절 여부, 기절 턴 수, 점수)
    board[s_r][s_c] = n # 산타 = n

# 산타의 번호가 주어지면 해당 산타의 좌표 (-1,-1)로 초기화, isfail=True로 변경
def fail_santa(santa_num):
    santa[santa_num][0] = -1
    santa[santa_num][1] = -1
    santa[santa_num][2] = True

# 산타의 위치와 이동 방향 -> 산타 기절 및 상호작용
def crash(rudolph_or_santa, santa_n, sx, sy, dsx, dsy, turn):
    E = 0
    dx, dy = 0, 0
    if rudolph_or_santa == 'r':
        E = C
        dx, dy = dsx, dsy
    else:
        E = D
        dx, dy = -dsx, -dsy

    # 산타 점수 획득 및 밀려남
    crash_santa = santa_n
    santa[crash_santa][5] += E
    n_sx = sx + dx * E
    n_sy = sy + dy * E
    # 범위 내 -> 기절 & 상호작용
    if 1 <= n_sx <= N and 1 <= n_sy <= N:
        # 산타 이동 & 기절
        santa[crash_santa][0] = n_sx
        santa[crash_santa][1] = n_sy
        santa[crash_santa][3] = True
        santa[crash_santa][4] = turn
        while board[n_sx][n_sy] != '.':  # 상호작용
            next_crash_santa = board[n_sx][n_sy]
            board[n_sx][n_sy] = crash_santa
            n_sx += dx
            n_sy += dy
            crash_santa = next_crash_santa
            if 1 <= n_sx <= N and 1 <= n_sy <= N:
                santa[crash_santa][0] = n_sx
                santa[crash_santa][1] = n_sy
            else:
                fail_santa(crash_santa)
                break
        else: board[n_sx][n_sy] = crash_santa  # 보드에 산타 자리 변경
    # 1-3-2) 범위 밖 -> 탈락
    else: fail_santa(crash_santa)

for m in range(M): # M번 턴 수행
    # 1) 루돌프 이동
    # 1-1) 가장 가까운 산타 찾기
    close_santa = []
    for n, s in enumerate(santa[1:], 1):
        r, c, is_fail, is_faint, faint_cnt, score = s
        if is_fail: continue # 탈락한 산타 pass
        d = (r_r - r)**2 + (r_c - c)**2
        close_santa.append([d, r, c])
    close_santa.sort(key=lambda x:(x[0], -x[1], -x[2]))
    cs_r, cs_c = close_santa[0][1], close_santa[0][2]

    # 1-2) 루돌프는 가장 가까운 방향으로 돌진
    dx, dy = 0, 0
    if r_r - cs_r > 0: dx = -1
    elif cs_r - r_r > 0: dx = 1
    if r_c - cs_c > 0: dy = -1
    elif cs_c - r_c > 0: dy = 1
    board[r_r][r_c] = '.'
    r_r, r_c = r_r + dx, r_c + dy
    # 1-3) 산타와 충돌
    if board[r_r][r_c] != '.':
        crash('r', board[r_r][r_c], r_r, r_c, dx, dy, m)
    board[r_r][r_c] = 0 # 보드에 루돌프 자리 변경

    # 2) 산타 이동
    for n, s in enumerate(santa[1:], 1):
        r, c, is_fail, is_faint, faint_cnt, score = s
        if is_fail: continue
        if is_faint:
            if faint_cnt + 2 != m: continue
            else:
                santa[n][3] = False
                santa[n][4] = 0
        # 가장 가까운 방향 찾기
        next_santa = []
        for i, (dx, dy) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
            nx, ny = r + dx, c + dy
            if 1 <= nx <= N and 1 <= ny <= N and (board[nx][ny] == 0 or board[nx][ny] == '.'):
                if (r-r_r)**2 + (c-r_c)**2 > (nx-r_r)**2 + (ny-r_c)**2:
                    next_santa.append([(nx-r_r)**2 + (ny-r_c)**2, i, nx,ny,dx,dy])
        if len(next_santa) == 0: continue
        # 산타 이동
        next_santa.sort(key=lambda x:(x[0], x[1]))
        board[r][c] = '.'
        s_r, s_c, dx, dy = next_santa[0][2], next_santa[0][3], next_santa[0][4], next_santa[0][5]
        # 루돌프와 충돌
        if board[s_r][s_c] == 0:
            crash('s', n, s_r, s_c, dx, dy, m)
        else:
            santa[n][0] = s_r
            santa[n][1] = s_c
            board[s_r][s_c] = n

    # 3) 탈락 안하면 산타 +1 점
    cnt = 0
    for n, s in enumerate(santa[1:], 1):
        r, c, is_fail, is_faint, faint_cnt, score = s
        if is_fail: continue
        santa[n][5] += 1
        cnt += 1
    if cnt == 0: break

# 산타가 얻은 최종 점수
print(*list(zip(*santa[1:]))[5])