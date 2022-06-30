import sys
input = sys.stdin.readline

N = int(input())
small, big = N // 5, N // 3
n = 0
answer = -1

while n <= small:
    res = N - 5*(small - n)
    if res % 3 == 0:
        answer = (small - n) + (res // 3)
        break
    n += 1
print(answer)