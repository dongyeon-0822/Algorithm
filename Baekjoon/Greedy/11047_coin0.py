import sys
input = sys.stdin.readline

N, K = map(int, input().split())
value = []
for i in range(N):
    value.append(int(input()))
count = 0
for v in reversed(value):
    if K != 0:
        count += (K // v)
        K %= v
print(count)