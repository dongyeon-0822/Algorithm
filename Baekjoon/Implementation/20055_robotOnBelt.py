import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = [[False,x] for x in list(map(int, input().split()))] # [isRobot, durability]

count = 0
while True:
    count += 1
    # step 1
    belt = [belt[-1]] + belt[:-1]
    belt[N-1][0] = False # 내리는 위치는 무조건 내리기

    # step 2
    for i in range(2*N - 2,-1,-1):
        if belt[i][0] and not belt[i+1][0] and belt[i+1][1] >= 1:
            belt[i][0] = False
            belt[i+1][0] = True
            belt[i+1][1] -= 1
    belt[N - 1][0] = False  # 내리는 위치는 무조건 내리기

    # step 3
    if belt[0][1] != 0:
        belt[0][0] = True
        belt[0][1] -= 1

    # step 4
    if list(zip(*belt))[1].count(0) >= K:
        break
print(count)