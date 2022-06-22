def solution(n):
    answer = 0
    tmp = 0
    for a in range(1,int(n/2)+1):
        for b in range(a,a + int(n/2)+1):
            tmp += b
            if tmp == n:
                answer += 1
                tmp = 0
                break
            elif tmp > n:
                tmp = 0
                break
    return answer+1

solution(15)