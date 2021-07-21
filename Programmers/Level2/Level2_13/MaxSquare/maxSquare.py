def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])

    for i in range(min(row,col), 0, -1): # 한 변의 길이
        for r in range(0,row+1-i):
            for c in range(0,col+1-i):
                flag = 1
                for _r in range(r, r + i):
                    for _c in range(c, c + i):
                        if board[_r][_c] == 0:
                            flag = 0
                            break
                    if not flag: break
                if flag:
                    return i*i
    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))