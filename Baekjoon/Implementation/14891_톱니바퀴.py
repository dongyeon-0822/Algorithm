import sys
from collections import deque
input = sys.stdin.readline

wheels = [deque(map(int,input().rstrip())) for _ in range(4)]
k = int(input())
commands = [list(map(int, input().split())) for _ in range(k)]
state = [[] for _ in range(4)]

for n, direct in commands:
    for i in range(4):
        state[i] = [wheels[i][6], wheels[i][2]]  # left, right
    left, right = state[n-1][0], state[n-1][1] # 현재 톱니 바퀴 상태
    wheels[n-1].rotate(direct)

    left_goStop, right_goStop = True, True
    left_wheel, right_wheel = n - 2, n # 양 옆 톱니 바퀴
    left_direct, right_direct = direct, direct # 양 옆 회전 방향
    while left_goStop and left_wheel >= 0 or right_goStop and right_wheel < 4:
        if left_goStop and left_wheel >= 0:
            if state[left_wheel + 1][0] != state[left_wheel][1]:
                wheels[left_wheel].rotate(-left_direct)
                left_wheel -= 1
                left_direct *= -1
            else: left_goStop = False
        if right_goStop and right_wheel < 4:
            if state[right_wheel - 1][1] != state[right_wheel][0]:
                wheels[right_wheel].rotate(-right_direct)
                right_wheel += 1
                right_direct *= -1
            else: right_goStop = False

answer = 0
for i, wheel in enumerate(wheels):
    if wheel[0]: answer += 2 ** i
print(answer)