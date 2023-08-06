import sys
from bisect import bisect_right
input = sys.stdin.readline

answer = []
N, M = map(int, input().split())
books = sorted(list(map(int, input().split())))
start = bisect_right(books, 0)
left_books = books[0:start]
right_books = books[N-1:start-1:-1] if start != 0 else books[::-1]

for i in range(0, len(left_books), M):
    answer.append(abs(left_books[i]) * 2)
for i in range(0, len(right_books), M):
    answer.append(right_books[i] * 2)

print(sum(answer)-max(answer)//2)



