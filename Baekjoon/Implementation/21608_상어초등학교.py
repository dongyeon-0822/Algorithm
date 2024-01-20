import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
seat = [[0] * N for _ in range(N)]
empty_seat = {(i,j):True for j in range(N) for i in range(N)}

likes = {}
for _ in range(N*N):
    arr = list(map(int, input().split()))
    n, n_likes = arr[0], arr[1:]
    likes[n] = n_likes

    # 자리 정하기
    # 조건 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로
    likes_cnt = defaultdict(list)
    for x, y in empty_seat:
        cnt = 0
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]: # 인접한 칸에 좋아하는 학생 세기
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] in n_likes:
                    cnt += 1
        likes_cnt[cnt].append((x, y))
    max_likes_cnt = likes_cnt[max(likes_cnt.keys())]
    if len(max_likes_cnt) == 1:
        x, y = max_likes_cnt[0]
        seat[x][y] = n
        del empty_seat[(x,y)]
        continue
    else: # 조건 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
        empty_cnt = defaultdict(list)
        for x, y in max_likes_cnt:
            cnt = 0
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 인접한 칸에 빈 자리 세기
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if seat[nx][ny] == 0:
                        cnt += 1
            empty_cnt[cnt].append((x, y))
        max_empty_cnt = empty_cnt[max(empty_cnt.keys())]
        if len(max_empty_cnt) == 1:
            x, y = max_empty_cnt[0]
            seat[x][y] = n
            del empty_seat[(x, y)]
            continue
        else: # 조건 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸
            max_empty_cnt.sort()
            x,y = max_empty_cnt[0]
            seat[x][y] = n
            del empty_seat[(x, y)]
# 학생의 만족도 구하기
answer = 0
satisfaction = [0,1,10,100,1000]
for x in range(N):
    for y in range(N):
        cnt = 0
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if seat[nx][ny] in likes[seat[x][y]]:
                    cnt += 1
        answer += satisfaction[cnt]
print(answer)