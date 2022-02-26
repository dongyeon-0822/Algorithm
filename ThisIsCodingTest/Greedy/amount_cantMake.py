from itertools import combinations


N = int(input())
coin = list(map(int, input().split()))

arr = []
for n in range(N):
    tmp = [sum(t) for t in combinations(coin, n + 1)]
    arr.extend(tmp)
arr = list(set(arr))
answer = 1
while True:
    if answer not in arr:
        break
    answer += 1
print(answer)