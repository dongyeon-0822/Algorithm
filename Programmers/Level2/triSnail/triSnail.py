def solution(n):
    answer = []
    arr=[[0 for j in range(i+1)] for i in range(n)]

    x,y,num=-1,0,1
    for i in range(n):
        if i%3==0:
            for j in range(n-i):
                x+=1
                arr[x][y]=num
                num+=1
        elif i%3==1:
            for j in range(n-i):
                y+=1
                arr[x][y]=num
                num+=1
        else:
            for j in range(n-i):
                x-=1
                y-=1
                arr[x][y]=num
                num+=1
    for i in arr:
        answer.extend(i)
    return answer

print(solution(5))