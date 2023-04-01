def solution(board):
    count_O = 0
    count_X = 0
    win_O = 0
    win_X = 0

    for row, col in zip(board, list(zip(*board))):
        # 후공, 선공 개수 세기
        count_O += row.count('O')
        count_X += row.count('X')

        # 가로, 세로 같은지 확인
        if len(set(row)) == 1:
            if row[0] == 'O':
                win_O += 1
            elif row[0] == 'X':
                win_X += 1
        if len(set(col)) == 1:
            if col[0] == 'O':
                win_O += 1
            elif col[0] == 'X':
                win_X += 1

    # 대각선 확인
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            win_O += 1
        elif board[0][0] == 'X':
            win_X += 1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            win_O += 1
        elif board[0][2] == 'X':
            win_X += 1

    # 승자가 여러 명인 경우
    if win_O > 0 and win_X > 0:
        return 0
    # 후공이 먼저 놓은 경우
    if count_O - count_X < 0 or count_O - count_X > 1 :
        return 0
    # O가 이기고 X가 둔 경우
    if count_O == count_X and win_O > 0 and win_X == 0:
        return 0
    # X가 이기고 O가 둔 경우
    if count_O > count_X and win_X > 0 and win_O == 0:
        return 0
    return 1

print(solution(["XXX", "XOO", "OOO"]))