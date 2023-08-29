import sys
input = sys.stdin.readline
from collections import deque

N, M, R = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

lines = []
min_num = min(N,M)
arr_col = list(zip(*arr))
for x in range(min_num//2): # 회전하는 라인은 일차원 배열로 뽑기
    line = []
    line.extend(arr[x][x:M-x])
    line.extend(arr_col[M-1-x][x+1:N-x])
    line.extend(arr[N-1-x][::-1][x+1:M-x])
    line.extend(arr_col[x][::-1][x+1:N-x-1])
    lines.append(line)

new_lines = []
for line in lines: # 일차원 배열을 회전
    r = R % len(line)
    line = line[r:] + line[:r]
    new_lines.extend(line)

# answer 배열 만들기
answer = [[0]*M for i in range(N)]

row, column, idx = 0, -1, -1
row_size, column_size = N, M
direction = 1

while row_size and column_size: # 달팽이 모양으로 배열 만들기
    for _ in range(column_size):
        idx += 1
        column += direction
        answer[row][column] = new_lines[idx]
    row_size -= 1

    for _ in range(row_size):
        idx += 1
        row += direction
        answer[row][column] = new_lines[idx]
    column_size -= 1

    direction *= -1

for i in range(N):
    for j in range(M):
        if j == M-1:
            print(answer[i][j], end="")
        else:
            print(answer[i][j], end=" ")
    print()