def solution(n):
    answer = []
    arr=[[0 for j in range(i+1)] for i in range(n)]

    x,y,num=0,0,0
    for i in range(n):
        if i%3==1:
            for j in range(n-i):
                arr[x][y]=num
    return answer