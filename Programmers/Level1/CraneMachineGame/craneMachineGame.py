def solution(board, moves):
    answer = 0
    stack=[]
    for i in moves:
        deep=0
        while deep<len(board):
            if board[deep][i-1]!=0:
                if len(stack)==0:
                    stack.append(board[deep][i-1])
                elif stack[-1] != board[deep][i - 1]:
                    stack.append(board[deep][i - 1])
                elif stack[-1]==board[deep][i-1]:
                    stack.pop()
                    answer+=2
                board[deep][i - 1]=0
                break;
            else: deep+=1
    return answer

if __name__ =='__main__':
    board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves=[1,5,3,5,1,2,1,4]
    print(solution(board,moves))