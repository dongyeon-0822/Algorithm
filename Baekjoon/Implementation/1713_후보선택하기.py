import sys
input = sys.stdin.readline

N = int(input())
recommend = int(input())
students = list(map(int, input().split()))

pictures = dict() # {student: [추천수, 게시날]}
for i, student in enumerate(students):
    if student in pictures:
        pictures[student][0] += 1
        continue
    if len(pictures) >= N:
        tmp = sorted(pictures.items(), key=lambda x: x[1])
        del pictures[tmp[0][0]]
    pictures[student] = [1, i]
answer = sorted(pictures.keys())
print(*answer)