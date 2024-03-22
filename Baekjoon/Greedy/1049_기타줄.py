import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prices = [list(map(int, input().split())) for _ in range(M)]

answer = 0
q, r = N // 6, N % 6
bunch, item = zip(*prices)
min_bunch, min_item = min(bunch), min(item)
if min_item * 6 < min_bunch:
    answer += min_item * N
else:
    answer = min(min_bunch*q + min_item*r, min_bunch*(q+1))
print(answer)