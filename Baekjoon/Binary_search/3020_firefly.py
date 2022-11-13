from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
down_obstacle = []
up_obstacle = []
for i in range(N):
    if i%2 == 0:
        down_obstacle.append(int(input()))
    else:
        up_obstacle.append(H - int(input()))
down_obstacle.sort()
up_obstacle.sort()

cnt = [0] * (H+1)
for i in range(1,H+1):
    cnt[i] = (N//2 - bisect_left(down_obstacle,i)+bisect_left(up_obstacle,i))

min_cnt = cnt[1]
answer = 0
for c in cnt[1:]:
    if min_cnt > c:
        min_cnt = c
        answer = 1
    elif min_cnt == c:
        answer += 1
print(min_cnt, answer)
