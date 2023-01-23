import sys
input = sys.stdin.readline

N = int(input())
board = [-1]*N
answer = 0

def promising(col):
    for c in range(col):
        if board[c] == board[col] or abs(c-col) == abs(board[c]-board[col]):
            return False
    return True

def nQueens(row):
    global answer
    if row == N:
        answer += 1
        return
    for c in range(N): # 각 열마다 Queen 놓기
        board[row] = c
        if promising(row):
            nQueens(row+1)

nQueens(0)
print(answer)