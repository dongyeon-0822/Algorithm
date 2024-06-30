import sys
input = sys.stdin.readline

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
answer = []

def backtracking(seed, visited, price, i, j):
    if seed == 3: # 종료 조건
        answer.append(price)
        return
    if seed < 3 and (i > N - 2 or j > N - 2):
        return

    for x in range(1, N-1):
        for y in range(1, N-1):
            price_tmp = 0
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x, y)]:
                price_tmp += field[nx][ny]
                if (nx, ny) in visited: break
            else:
                new_visited = visited.union({(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x, y)})
                nny = 1 if y + 1 == N-1 else y + 1
                nnx = x + 1 if nny == 1 else x
                backtracking(seed+1, new_visited, price+price_tmp, nnx, nny)

backtracking(0, set(), 0, 1, 1)
# print(answer)
print(min(answer))