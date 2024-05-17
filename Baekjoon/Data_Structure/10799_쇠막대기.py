import sys
input = sys.stdin.readline

brackets = input().rstrip()
answer = 0
ex = brackets[0]
cnt = 1
stick_cnt = 1 if ex == '(' else 0
for x in brackets[1:]:
    if ex == '(' and x == ')': # 레이저인 경우
        cnt -= 1
        stick_cnt -= 1
        answer += cnt
    elif x == '(':
        cnt += 1
        stick_cnt += 1
    else:
        cnt -= 1
    ex = x
print(answer + stick_cnt)