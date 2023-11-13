import sys
input = sys.stdin.readline

N = int(input())
testcase = [int(input()) for _ in range(N)]

for i, t in enumerate(testcase, 1):
    print('#'+ str(i))
    snail = [[0]*t for _ in range(t)]
    direct = [[0,1], [1,0], [0,-1], [-1,0]]

    n = 1
    d = 0
    dx, dy = direct[d]
    x, y = 0, -1
    while n <= t * t:
        x, y = x + dx, y + dy
        if 0 <= x < t and 0 <= y < t and snail[x][y] == 0:
            snail[x][y] = n
        else:
            x, y = x - dx, y - dy
            d = (d+1) % 4
            dx, dy = direct[d]
            x, y = x + dx, y + dy
            snail[x][y] = n
        n += 1
    for row in snail:
        print(*row)