if __name__ =='__main__':
    board = input()
    X = [x for x in board.split('.') if x!='']
    _X = []
    for x in X:
        pm = ''
        if len(x)%2!=0:
            print(-1)
            exit()
        else:
            pm += (len(x)//4)*'AAAA'
            pm += (len(x)%4//2)*'BB'
            _X.append(pm)
    for i,x in enumerate(_X):
        board=board.replace(X[i],x,1)
    print(board)