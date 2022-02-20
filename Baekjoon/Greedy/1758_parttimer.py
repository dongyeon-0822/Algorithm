import sys
input = sys.stdin.readline

N = int(input())
tip = []
for i in range(N):
    tip.append(int(input()))
tip.sort(reverse=True)
result = [x - i for i, x in enumerate(tip) if (x - i) > 0]
print(sum(result))