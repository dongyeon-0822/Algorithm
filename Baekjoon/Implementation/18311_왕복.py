import sys
input = sys.stdin.readline

N, K = map(int, input().split())
course = list(map(int, input().split()))
total = sum(course)

if K < total:
    distance = 0
    for i, n in enumerate(course, 1):
        distance += n
        if distance - n <= K < distance:
            print(i)
            break
else:
    distance = total
    for i, n in enumerate(course[::-1]):
        distance += n
        if distance - n <= K < distance:
            print(N - i)
            break