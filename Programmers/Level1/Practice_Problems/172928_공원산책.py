def solution(park, routes):
    answer = []
    S = []
    X = []
    direction = {'N':[-1,0], 'S':[1,0], 'W':[0,-1], 'E':[0,1]}

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                S = [i,j]
            elif park[i][j] == 'X':
                X.append([i,j])

    x,y = S
    for route in routes:
        op, n = route.split()
        n = int(n)
        dx, dy = direction[op]
        noPass = False
        for i in range(1,n+1):
            nx = x + dx * i
            ny = y + dy * i
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
                noPass = True
                break
            if park[nx][ny] == 'X':
                noPass = True
                break
        if noPass:
            continue
        else:
            x += dx * n
            y += dy * n
    answer = [x,y]

    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))