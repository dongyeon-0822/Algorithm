import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
rotates = [list(input().split()) for _ in range(L)]
directs = [[-1, 0], [0, -1], [1, 0], [0, 1]] # 상, 좌, 하, 우


x, y = 1, 1 # 뱀의 머리 위치
time = 0 # 게임 시간
snake = deque() # 뱀의 모든 위치
direct = 3 # 뱀의 방향
rotate = 0 # rotates 의 인덱스

# 벽 또는 자기 자신과 부딪힐 때까지 반복
snake.append([x,y])
while True:
    # 방향 전환 확인
    if rotate < len(rotates) and time == int(rotates[rotate][0]):
        if rotates[rotate][1] == 'L':
            direct += 1
        else:
            direct -= 1
        if direct == -1:
            direct = 3
        if direct == 4:
            direct = 0
        rotate += 1
    # 머리 이동
    _x, _y = directs[direct]
    x += _x
    y += _y
    # 종료 조건 확인
    if x < 1 or x > N or y < 1 or y > N or [x,y] in snake:
        break

    snake.append([x, y])  # 머리 늘리기
    # 사과 있는지 확인
    if [x, y] in apples:
        apples.remove([x, y])  # 사과 먹기
    else:
        snake.popleft()  # 꼬리 줄이기

    time += 1
print(time+1)

