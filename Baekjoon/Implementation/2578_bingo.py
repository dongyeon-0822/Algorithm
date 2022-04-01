import sys
input = sys.stdin.readline

board = []
for i in range(5):
    line = list(map(int, input().split()))
    board.append(line)

bingo = 0
diagonal_1 = [(0,0), (1,1), (3,3), (4,4)]
diagonal_2 = [(4,0), (3,1), (1,3), (0,4)]
for i in range(5):
    flag_ = 0
    line = list(map(int, input().split()))
    for l in line: # 입력받은 숫자 하나
        flag = 0
        for row,b in enumerate(board): # 보드에 있는지
            if l in b:
                col = b.index(l)
                b[col] = 0
                # 빙고 확인
                if sum(b) == 0: # 가로
                    bingo += 1
                if sum([x[col] for x in board]) == 0: # 세로
                    bingo += 1
                if row == 2 and col == 2: # 대각선 둘다 검사
                    if sum(board[x][x] for x in range(5)) == 0:
                        bingo += 1
                    if sum(board[x][4-x] for x in range(5)) == 0:
                        bingo += 1
                elif (row, col) in diagonal_1 and sum(board[x][x] for x in range(5)) == 0:
                    bingo += 1
                elif (row, col) in diagonal_2 and sum(board[x][4-x] for x in range(5)) == 0:
                    bingo += 1
                if bingo >= 3:
                    print((i+1)*5 + col + 1)
                    flag = 1
                    break
        if flag:
            flag_ = 1
            break
    if flag_:
        break
