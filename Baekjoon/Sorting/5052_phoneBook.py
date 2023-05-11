import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input().rstrip() for _ in range(n)]
    answer = True
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1].startswith(numbers[i]):
            answer = False
            break
    if answer:
        print("YES")
    else:
        print("NO")