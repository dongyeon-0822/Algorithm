import sys
from collections import deque
input = sys.stdin.readline

MAX_DISTANCE = 1000 # 20 * 50

def bfs(start, end, nodes):
    q = deque()
    q.append(start)

    while q:
        x,y = q.popleft()
        if abs(end[0] - x) + abs(end[1] - y) <= MAX_DISTANCE: # end 까지 도달할 수 있다면
            return True
        for node in nodes: # 편의점을 돌면서 방문할 수 있는 편의점을 큐에 추가한다.
            distance = abs(node[0] - x) + abs(node[1] - y)
            if not node[2] and distance <= MAX_DISTANCE:
                node[2] = True
                q.append([node[0],node[1]])
    return False

test_case = int(input())
for _ in range(test_case):
    market = int(input())
    home = list(map(int, input().split()))
    markets = [list(map(int, input().split())) + [False] for _ in range(market)]
    festival = list(map(int, input().split()))

    if bfs(home, festival, markets):
        print("happy")
    else:
        print("sad")