import sys
input = sys.stdin.readline

S = input().rstrip()

cnt = 0
prev = S[0]
for s in S[1:]:
    if prev != s:
        prev = s
        cnt += 1
print(cnt // 2 + cnt % 2)