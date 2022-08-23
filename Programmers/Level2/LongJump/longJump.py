# 왜 틀렸는지 모르겠지만 테케 7부터 실패
# import math
# def solution(n):
#     answer = 1
#     for i in range(1, n//2 + 1):
#         one = n - 2*i
#         two = i
#         tmp = math.factorial(one + two)
#         tmp /= math.factorial(one)
#         tmp /= math.factorial(two)
#         answer %= 1234567
#         answer += tmp
#     return answer % 1234567

# DP로 풀어보기
# DP 중에서도 반복문을 이용해야 정답

global arr
arr = [0]*2001
arr[1] = 1
arr[2] = 2
def fibonacci(n):
    if arr[n] != 0:
        return arr[n]
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n] % 1234567

def solution(n):
    return fibonacci(n)
