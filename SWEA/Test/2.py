from collections import deque, Counter


T = int(input())
answer = []
for _ in range(T):
    N, A, B = map(int, input().split())
    score = list(map(int, input().split()))
    high, mid, low = 0,0,0

    score_count = Counter(score)
    score_keys = sorted(score_count.keys(), reverse=True)
    h, l = 0, len(score_keys) - 1
    while True:
        high += sum([score_count[score_keys[h]] for h in range(0,h+1)])
        low += sum([score_count[score_keys[l]] for l in range(l, len(score_keys))])
        mid = N - (high + low)
        if A <= mid - score_count[score_keys[h+1]] <= B:
            h += 1
        elif A <= mid - score_count[score_keys[l-1]] <= B:
            l -= 1

        if A <= mid <= B: break

    answer.append(mid)

for i, a in enumerate(answer, 1):
    print("#" + str(i), a)