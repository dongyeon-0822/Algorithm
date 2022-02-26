N = int(input())
fear = list(map(int, input().split()))

fear.sort(reverse=True)
i = 0
answer = 0
while i < len(fear):
    i += fear[i]
    answer += 1
print(answer)