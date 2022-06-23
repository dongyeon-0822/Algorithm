import sys
input = sys.stdin.readline

def check_bingo(check_board):
    bingo = 0
    for row in check_board: # 가로
        if sum(row) == 5:
            bingo += 1
            if bingo == 3:
                return True
    for col in range(5): # 세로
        if sum(list(zip(*check_board))[col]) == 5:
            bingo += 1
            if bingo == 3:
                return True
    if check_board[0][0]==check_board[1][1]==check_board[2][2]==check_board[3][3]==check_board[4][4]==1:
        bingo += 1
        if bingo == 3:
            return True
    if check_board[0][4]==check_board[1][3]==check_board[2][2]==check_board[3][1]==check_board[4][0]==1:
        bingo += 1
        if bingo == 3:
            return True

dic = {}
for i in range(5):
    line = list(map(int, input().split()))
    for j, l in enumerate(line):
        dic[l] = (i,j)

board = [[0]*5 for _ in range(5)]
count = 0
for i in range(5):
    line = list(map(int, input().split()))
    flag = False
    for j, l in enumerate(line):
        count += 1
        r,c = dic[l]
        board[r][c] = 1
        if count >= 12 and check_bingo(board):
            print(count)
            flag = True
            break
    if flag:
        break