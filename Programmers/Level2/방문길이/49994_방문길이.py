def solution(dirs):
    answer = 0

    dic = {'U' : (-1, 0), 'D' : (1, 0), 'R' : (0, 1), 'L' : (0, -1)}
    visited = set()

    x,y = 0,0
    for direct in dirs:
        dx, dy = dic[direct]
        nx, ny = x + dx, y + dy
        route = "".join(map(str, [x,y,nx,ny] if x < nx or y < ny else [nx,ny,x,y]))
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if route not in visited:
                visited.add(route)
                answer += 1
            x, y = nx, ny
    return answer

print(solution("RRRRRLLLLL"))