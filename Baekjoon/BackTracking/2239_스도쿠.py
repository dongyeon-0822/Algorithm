import sys
input = sys.stdin.readline


def dfs(count):
    if count == len(zeros):
        for line in sudoku:
            print(*line, sep="")
        sys.exit(0)

    r, c = zeros[count]
    promising = [False] * 10
    for i in range(9):
        if sudoku[r][i]: promising[sudoku[r][i]] = True
        if sudoku[i][c]: promising[sudoku[i][c]] = True
    for i in range(r//3*3, r//3*3 + 3):
        for j in range(c//3*3, c//3*3 + 3):
            if sudoku[i][j]:
                promising[sudoku[i][j]] = True

    for n in range(1,10):
        if not promising[n]:
            sudoku[r][c] = n
            dfs(count + 1)
            sudoku[r][c] = 0

sudoku = [list(map(int, input().rstrip())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
dfs(0)
