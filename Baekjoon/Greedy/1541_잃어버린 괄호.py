import sys
import re
input = sys.stdin.readline

line = input().rstrip()
sign = [l for l in line if l == '+' or l == '-']
num = list(map(int,re.split('[+-]', line)))

answer = num[0]
flag = True
for i in range(len(sign)):
    if sign[i] == '+' and flag: # + + 일때
        answer += num[i+1]
    elif sign[i] == '+' and not flag: # - + 일때
        answer -= num[i+1]
    elif sign[i] == '-' and flag: # + - 일때
        flag = False
        answer -= num[i+1]
    elif sign[i] == '-' and not flag: # - - 일때
        answer -= num[i+1]

print(answer)
