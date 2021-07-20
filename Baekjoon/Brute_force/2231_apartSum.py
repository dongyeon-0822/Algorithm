if __name__=='__main__':
    n = input()
    N = int(n)
    flag = 0
    M_arr=[]
    start = N-len(n)* 9
    if start <=0 :
        start = 1
    for i in range(start,N):
        M = i+sum(map(int,str(i)))
        if N==M:
            M_arr.append(i)
            flag = 1
            break
    if flag:
        print(min(M_arr))
    else:
        print(0)