import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

lp, rp = 0, N-1
answer = int(1e9)
while lp != rp:
    answer = liquid[lp] + liquid[rp] if abs(answer) > abs(liquid[lp] + liquid[rp]) else answer
    if liquid[lp] + liquid[rp] > 0: rp -= 1
    else: lp += 1

print(answer)