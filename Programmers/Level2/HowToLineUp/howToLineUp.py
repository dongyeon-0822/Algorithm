from math import factorial
def solution(n, k):
    answer = []
    arr = list(range(1,n+1))
    k -= 1
    while n:
        num = k // factorial(n-1) # 몫
        k %= factorial(n-1) # 나머지
        answer.append(arr[num])
        arr.pop(num)
        n -= 1
    return answer


