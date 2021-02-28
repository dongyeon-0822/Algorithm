def solution(n):
    answer = 0
    arr=[]
    while n>0:
        arr.append(n%3)
        n//=3
    arr.reverse()
    for i in range(len(arr)):
        answer+=arr[i]*3**i
    return answer

print(solution(45))