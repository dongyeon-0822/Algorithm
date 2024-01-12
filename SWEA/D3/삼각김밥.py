import sys
from collections import deque
input = sys.stdin.readline

dic = {} # n : (x,y)
arr = []
n = 1
row = 0
while n <= 10000:
    line = []
    col = 0
    while col <= row:
        dic[n] = (row, col)
        line.append(n)
        n += 1
        col += 1
    row += 1
    arr.append(line)
print(dic)

T = int(input())
for t in range(1, T+1):
    answer = 0
    s,e = map(int, input().split())
    start, end = min(s,e), max(s,e)

    visited = [False] * 100001
    q = deque()
    q.append((dic[start], 0))
    visited[start] = True
    while q:
        (x, y), d = q.popleft()
        if arr[x][y] == end:
            answer = d
            break
        for dx, dy in [[0, -1], [0, 1], [1, 0], [1, 1]]:
            nx, ny = x + dx, y + dy
            if 0 <= ny <= nx < 140 and not visited[arr[nx][ny]]:
                q.append(((nx, ny), d+1))
                visited[arr[nx][ny]] = True

    print('#' + str(t), answer)