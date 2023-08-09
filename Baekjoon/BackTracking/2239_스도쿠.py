# 시간초과 미해결

import sys
input = sys.stdin.readline

def is_promising(row, col, num):
    if num in sudoku[row]:
        return False
    if num in list(zip(*sudoku))[col]:
        return False
    for x in range(row//3 * 3, row//3 * 3 + 3):
        for y in range(col//3 * 3, col//3 * 3 + 3):
            if num == sudoku[x][y]:
                return False
    return True

def print_sudoku(arr):
    for row in arr:
        for x in row:
            print(x, end="")
        print()

def dfs(r, c):
    if r == c == 8:
        print_sudoku(sudoku)
        return True
    nr = r + 1 if c == 8 else r
    nc = 0 if c == 8 else c + 1

    if sudoku[r][c] != 0:
        if dfs(nr, nc): return True
    else:
        for n in range(1,10):
            if is_promising(r,c,n):
                sudoku[r][c] = n
                if dfs(nr, nc): return True
        sudoku[r][c] = 0
    return False

sudoku = [list(map(int, input().rstrip())) for _ in range(9)]
dfs(0,0)
