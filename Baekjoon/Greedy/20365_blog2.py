import sys
input = sys.stdin.readline

N = int(input())
blog = input().rstrip()

tmp = blog[0]
cnt = 1
for i in range(1,N):
    if tmp != blog[i]:
        cnt += 1
        tmp = blog[i]
if cnt % 2:
    cnt -= (cnt//2)
else:
    cnt -= (cnt//2 - 1)
print(cnt)