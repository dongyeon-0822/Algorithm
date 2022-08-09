import sys
input = sys.stdin.readline

keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
dic = {}
for i, line in enumerate(keyboard):
    for j, l in enumerate(line):
        if (i < 2 and j > 4) or (i == 2 and j > 3):
            dic[l] = ['R', (i, j)]
        else:
            dic[l] = ['L', (i, j)]

left, right = map(lambda x:dic[x][1], input().split())
line = input().strip()
answer = 0

for l in line:
    answer += 1
    if dic[l][0] == 'L':
        answer += abs(dic[l][1][0] - left[0]) + abs(dic[l][1][1] - left[1])
        left = dic[l][1]
    else:
        answer += abs(dic[l][1][0] - right[0]) + abs(dic[l][1][1] - right[1])
        right = dic[l][1]
print(answer)