import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    if start == K: # 예외처리!!
        return 0
    q.append([start, 0])
    visited[start] = True

    sec = 0
    while q:
        k, sec = q.popleft()
        next_k = [2*k, k-1,k+1]
        for i,n in enumerate(next_k):
            if n == K: # 답이라면
                if i != 0:
                    return sec + 1
                return sec
            if 0<=n<=100000 and not visited[n]: # 답이 아니라면
                visited[n] = True
                if i != 0:
                    q.append([n, sec+1])
                else:
                    q.append([n, sec])
    return sec

N, K = map(int, input().split())
q = deque()
visited = [False] * 100001

print(bfs(N))



