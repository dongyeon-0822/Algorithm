from collections import deque
import sys
sys.stdin = open("input.txt", "r")

L, N, Q = map(int, input().split())
chess = [[0]*(L+1)] # 0:빈칸, 1:함정, 2:벽
for _ in range(L):
    chess.append([0]+list(map(int, input().split())))
knights_in_chess = [[0]*(L+1) for _ in range(L+1)]
knights = [[] for _ in range(N+1)] # [r,c,h,w,k,d,flag]
for n in range(1, N+1):
    r,c,h,w,k = knight = list(map(int, input().split()))
    knights[n] = knight + [0, False]
    for i in range(r, r + h):
        for j in range(c, c + w):
            knights_in_chess[i][j] = n

directs = [(-1,0), (0,1), (1,0), (0,-1)]
for _ in range(Q):
    n, d = map(int, input().split()) # n번 기사 d방향 이동 명령
    if knights[n][6]: continue # 사라진 기사라면 pass

    tmp_knights_in_chess = [line[:] for line in knights_in_chess]
    tmp_knights = [k[:] for k in knights]

    q = deque()
    can_move = True
    first_move = True
    dx, dy = directs[d]
    q.append([n] + knights[n])
    while can_move and q:
        n, r, c, h, w, k, d, f = q.popleft()
        damage = 0
        now_range = [(i,j) for i in range(r, r + h) for j in range(c, c + w)]
        next_range = []
        for i, j in now_range:
            nx, ny = i + dx, j + dy
            if not (1 <= nx <= L and 1 <= ny <= L): # 벽인 경우
                can_move = False
                break
            if chess[nx][ny] == 2: # 벽인 경우
                can_move = False
                break
            if tmp_knights_in_chess[nx][ny] != 0 and tmp_knights_in_chess[nx][ny] != n: # 기사인 경우
                nn = tmp_knights_in_chess[nx][ny]
                q.append([nn] + knights[nn])
            if chess[nx][ny] == 1: # 함정인 경우
                damage += 1
            next_range.append((nx, ny))
        if not can_move: break
        # 체스판에서 기사 위치 변경
        inter_set = list(set(next_range) & set(now_range))
        differ_set_now = list(set(now_range) - set(next_range))
        differ_set_next = list(set(next_range) - set(now_range))
        for i,j in differ_set_now:
            if tmp_knights_in_chess[i][j] == n:
                tmp_knights_in_chess[i][j] = 0
        for i,j in inter_set + differ_set_next:
            tmp_knights_in_chess[i][j] = n
        # 기사 정보 변경
        if first_move: # 명령 받은 기사라면 데미지 X
            tmp_knights[n] = [r + dx, c + dy, h, w, k, d, f]
            first_move = False
        else:
            if d + damage >= k: # 데미지 >= 체력 -> 사라짐
                f = True
                # 체스판에서 삭제
                for i,j in next_range:
                    tmp_knights_in_chess[i][j] = 0
            tmp_knights[n] = [r + dx, c + dy, h, w, k, d + damage, f]
    else: # 이동 가능한 경우 업데이트
        knights_in_chess = [line[:] for line in tmp_knights_in_chess]
        knights = [k[:] for k in tmp_knights]

answer = 0
for r,c,h,w,k,d,f in knights[1:]:
    if not f:
        answer += d
print(answer)