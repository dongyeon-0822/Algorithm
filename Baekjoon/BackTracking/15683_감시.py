import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cctv = []
graph = []
directs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(n):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        if 1 <= r <= 5:
            cctv.append([r, i, j])
    graph.append(row)

def fill_direct(arr, direct, x, y):
    tmp_arr = [line[:] for line in arr]
    dx, dy = directs[direct]
    nx, ny = x + dx, y + dy
    while 0 <= nx < n and 0 <= ny < m and tmp_arr[nx][ny] != 6:
        if tmp_arr[nx][ny] == 0: tmp_arr[nx][ny] = '#'
        nx += dx
        ny += dy
    return tmp_arr

def fill_cctv(arr, types, direct, x, y):
    n_direct = direct
    tmp_arr = [line[:] for line in arr]
    if types == 1:
        tmp_arr = fill_direct(tmp_arr, n_direct, x, y)
    elif types == 2:
        tmp_arr = fill_direct(tmp_arr, n_direct, x, y)
        n_direct = (n_direct + 2) % 4 if n_direct + 2 > 3 else n_direct + 2
        tmp_arr = fill_direct(tmp_arr, n_direct, x, y)
    else: # 3, 4, 5
        for _ in range(types - 1):
            tmp_arr = fill_direct(tmp_arr, n_direct, x, y)
            n_direct = (n_direct + 1) % 4 if n_direct + 1 > 3 else n_direct + 1
    return tmp_arr

answers = []
def dfs(num, answer):
    if num == len(cctv): # 종료 조건
        cnt = 0
        for line in answer:
            cnt += line.count(0)
        answers.append(cnt)
        return

    # 현재 direct '#' 채우기
    t, x, y = cctv[num]
    scope = 4
    if t == 2: scope = 2
    elif t == 5: scope = 1
    for d in range(scope):
        tmp_answer = fill_cctv(answer, t, d, x, y)
        dfs(num + 1, tmp_answer)

answer = [row[:] for row in graph]
dfs(0, answer)
print(min(answers))