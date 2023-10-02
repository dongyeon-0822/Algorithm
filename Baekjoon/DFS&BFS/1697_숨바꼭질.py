import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 100001

q = deque()
q.append((0, N))
visited[N] = True
while q:
    d, x = q.popleft()
    if x == K:
        print(d)
        break
    for nx in [x + 1, x - 1, x * 2]:
        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            q.append((d + 1, nx))