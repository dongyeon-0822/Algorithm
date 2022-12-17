# 예외 처리
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = int(100*Y/X)

if X==Y:
    print(-1)
else:
    divisor = 99 - Z
    if divisor <= 0:
        print(-1)
    else:
        quantity = int(X*X / (99*X-100*Y))
        remain = (X*X % (99*X-100*Y))
        if remain == 0:
            print(quantity)
        else:
            print(quantity+1)