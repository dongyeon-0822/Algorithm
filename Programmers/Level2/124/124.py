def solution(n):
    answer = ''
    while n:
        if n%3==0:
            answer+='4'
            n-=3
        else: answer+=str(n%3)
        n//=3
    return answer[::-1]

print(solution(11))