import sys
input = sys.stdin.readline

N = int(input())
sale = []
for i in range(N):
    sale.append(int(input()))
sale.sort(reverse=True)
result = [x for i, x in enumerate(sale) if (i % 3) != 2]
print(sum(result))