import sys
from collections import Counter
input = sys.stdin.readline

n, d = map(int, input().split())
s = str(list(range(1, n+1)))
c = Counter(s)
print(c[str(d)])