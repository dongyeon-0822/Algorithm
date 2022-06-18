import sys
input = sys.stdin.readline

N = input()
drinks = list(map(int, input().split()))

drinks.sort(reverse=True)
answer = drinks[0]
for i in range(1, len(drinks)):
    answer += (drinks[i] / 2)
print(answer)