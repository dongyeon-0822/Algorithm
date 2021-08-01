def solution(n):
    answer = 0
    for a in range(1,n): # 2a+n = N+1
        flag = 0
        for num in range(2,n):
            if 2*a+num==n+1:
                answer+=1
                flag = 1
                break
        if flag:
            break
    return answer+1