import copy
def sort_0(x):
    if x=='0':
        return 0
    else:
        return 1
def solution(m, n, board):
    answer = 0
    board=[list(b) for b in board]
    while True:
        board_1 = copy.deepcopy(board)
        flag = True
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]!='0':
                    board_1[i][j]=board_1[i+1][j]=board_1[i][j+1]=board_1[i+1][j+1]='0'
                    flag = False
        if flag: break
        for j in range(n):
            arr = [r[j] for r in board_1]
            arr.sort(key=sort_0)
            for i in range(m):
                board_1[i][j]=arr[i]
        board = copy.deepcopy(board_1)
    for i in board:
        answer+=i.count('0')
    return answer

solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])