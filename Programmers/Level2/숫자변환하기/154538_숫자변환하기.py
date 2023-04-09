from collections import deque


def solution(x, y, n):
    answer = -1
    distance = [0] * 1000001
    q = deque()

    if x == y: return 0
    q.append(x)
    while q:
        x = q.popleft()
        for nx in [x+n, 2*x, 3*x]:
            if nx == y:
                return distance[x]+1
            if nx < 1000001 and distance[nx] == 0:
                q.append(nx)
                distance[nx] = distance[x]+1

    return answer

def solution2(x, y, n):
    answer = -1
    distance = [0] * (y+1)
    q = deque()

    if x == y: return 0
    q.append(y)
    while q:
        y = q.popleft()
        for ny, rest in [(y-n,0), (y//2, y%2), (y//3, y%3)]:
            if rest == 0 and ny == x:
                return distance[y]+1
            if rest == 0 and ny > 0 and distance[ny] == 0:
                q.append(ny)
                distance[ny] = distance[y]+1

    return answer