import sys
input = sys.stdin.readline

info = []
N = int(input())
for i in range(N):
    info.append(list(map(int, input().split())))
info.sort(key=lambda x : (x[1], x[0]))
count = 0
room = None
for i, r in enumerate(info):
    if i == 0:
        count += 1
        room = r
    elif r[0] >= room[1]:
        count += 1
        room = r
print(count)