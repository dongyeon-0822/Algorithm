import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    answer = 0
    n = int(input())
    agent = []
    if n < 3:
        for _ in range(n): input()
        answer = -1
    else:
        for _ in range(n):
            a,b,c = map(int,input().split())
            sum_abc = a+b+c
            a,b,c = sum_abc-a, sum_abc-b, sum_abc-c
            agent.append([a,b,c])
        min_sum = 0
        ability_set = []
        for a,b,c in agent:
            min_x = min(a, b, c)
            min_sum += min_x
            if [a,b,c].count(min_x) == 3:
                ability_set.append(0)
            elif [a,b,c].count(min_x) == 2:
                min_sum += min_x
            else:
                ability_set.append([a,b,c].index(min_x))





    print("#"+str(t), answer)