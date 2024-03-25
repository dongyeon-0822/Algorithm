import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, Q = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

for l in L:
    # 격자 나누고 회전
    tmp = [[-1] * (2 ** N) for _ in range(2 ** N)]
    length = 2**l
    for r in range(0, 2**N, length):
        for c in range(0, 2**N, length):
            for i in range(length):
                for j in range(length):
                    tmp[r+j][c+length-1-i] = ices[r+i][c+j]
    for r in range(2**N):
        ices[r] = tmp[r][:]
    # 얼음 줄어들기
    for r in range(2**N):
        for c in range(2**N):
            cnt = 0
            for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= x < 2**N and 0 <= y < 2**N and ices[x][y] > 0:
                    cnt += 1
            if cnt < 3:
                tmp[r][c] = ices[r][c] - 1
            else:
                tmp[r][c] = ices[r][c]
    for r in range(2**N):
        ices[r] = tmp[r][:]

# 남아있는 얼음 합
sum_ice = 0
for ice in ices:
    for i in ice:
        if i > 0:
            sum_ice += i
# 큰 덩어리 개수
max_ices = []
visited = [[False] * (2**N) for _ in range(2**N)]

def dfs(r, c):
    visited[r][c] = True
    count = 1
    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= x < 2 ** N and 0 <= y < 2 ** N and not visited[x][y] and ices[x][y] > 0:
            count += dfs(x, y)
    return count

for i in range(2**N):
    for j in range(2**N):
        if not visited[i][j] and ices[i][j] > 0:
            max_ices.append(dfs(i, j))
max_ice = max(max_ices) if max_ices else 0
print(sum_ice)
print(max_ice)