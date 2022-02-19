import sys
input = sys.stdin.readline

N = int(input())
length = list(map(int,input().split()))
price = list(map(int,input().split()))
p = price[0]
result = 0
for i in range(1,N):
    if p > price[i]:
        result += length[i - 1] * p
        p = price[i]
    else:
        result += length[i - 1] * p
print(result)