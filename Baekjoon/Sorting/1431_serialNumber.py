import sys
input = sys.stdin.readline

N = int(input())
serial = [input().rstrip() for _ in range(N)]
serial = sorted(serial, key=lambda x:(len(x), sum(map(int, [n for n in x if n.isdigit()])), x))

for s in serial:
    print(s)