T = int(input())

for t in range(1, T+1):
    n = int(input())
    agents = [list(map(int, input().split())) for _ in range(n)]
    agents.sort(key=lambda x: max(x), reverse=True)

    shared = [0, 0, 0]
    total = sum(map(sum, agents))

    for i in range(n):
        max_idx = agents[i].index(max(agents[i]))
        if i < 3:
            shared[i] = agents[i][max_idx]
        else:
            shared[max_idx] += agents[i][max_idx]
        agents[i][max_idx] = 0

    if all(shared):
        print("#" + str(t), total - sum(shared))
    else:
        print("#" + str(t),-1)
