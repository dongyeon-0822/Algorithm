# 답 참고함
import sys
input = sys.stdin.readline

global arr
arr = [0]*91

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if arr[n] != 0:
        return arr[n]
    arr[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return arr[n]

N = int(input())
print(fibonacci(N))