import sys
input = sys.stdin.readline

N = int(input())
filename = [input().strip() for _ in range(N)]

answer = ""
for i in range(len(filename[0])):
    tmp = list(zip(*filename))[i]
    if len(set(tmp)) == 1:
        answer+=tmp[0]
    else:
        answer+='?'
print(answer)