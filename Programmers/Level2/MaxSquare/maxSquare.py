def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])

    for r in range(1,row):
        for c in range(1,col):
            if board[r][c]:
                board[r][c]+=min(board[r-1][c-1],board[r-1][c],board[r][c-1])

    max_len=[]
    for lst in board:
        max_len.append(max(lst))
    return max(max_len)**2

print(solution(	[[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))