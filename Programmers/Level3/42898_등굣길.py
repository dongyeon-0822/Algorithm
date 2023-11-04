def solution(m, n, puddles):
    load = [[0] * (m+1) for _ in range(n+1)]

    load[1][1] = 1
    for i in range(2, n+1):
        if [1,i] in puddles: break
        load[i][1] = load[i-1][1]
    for j in range(2, m+1):
        if [j,1] in puddles: break
        load[1][j] = load[1][j-1]

    for i in range(2, n+1):
        for j in range(2, m+1):
            if [j, i] in puddles: continue
            load[i][j] = (load[i-1][j] + load[i][j-1]) % 1000000007
    print(load)
    return load[n][m]

print(solution(4,3,[[2,2]]))