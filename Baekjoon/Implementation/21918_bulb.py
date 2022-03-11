import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bulbs = list(map(int, input().split()))
for i in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        bulbs[b-1] = c
    elif a == 2:
        for j in range(b-1,c):
            bulbs[j] = int(not(bulbs[j]))
    elif a == 3:
        for j in range(b-1,c):
            bulbs[j] = 0
    elif a == 4:
        for j in range(b-1,c):
            bulbs[j] = 1
for b in bulbs:
    print(b, end=' ')