from itertools import permutations
N = input().strip()

answer = []
for p in permutations(N, len(N)):
    n = int(''.join(p))
    if n > int(N):
        answer.append(n)
answer.sort()
print(answer[0])