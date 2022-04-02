import sys
input = sys.stdin.readline

N, M = map(int, input().split())
DNA = []
for i in range(N):
    DNA.append(input().strip())
answer = ""
count = 0
for i in range(M):
    col = [x[i] for x in DNA]
    cnt = [0] * 4
    cnt[0] = col.count('A')
    cnt[1] = col.count('C')
    cnt[2] = col.count('G')
    cnt[3] = col.count('T')
    max_ = max(cnt)
    count += (N - max_)
    idx = cnt.index(max_)
    if idx == 0:
        answer += 'A'
    elif idx == 1:
        answer += 'C'
    elif idx == 2:
        answer += 'G'
    else:
        answer += 'T'
print(answer)
print(count)