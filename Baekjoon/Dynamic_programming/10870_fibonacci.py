import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
N = int(input())
print(fibonacci(N))
