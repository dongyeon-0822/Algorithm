import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m != 0: buttons = set(input().split())
case_1 = int(1e9)
case_2 = int(1e9)
answer = 0

# 모든 버튼이 고장난 경우 -> 100과의 차이
case_1 = abs(n-100)

# 남은 숫자로 n에 가장 가까운 수 만들기
if m == 0: # 고장난 버튼이 없는 경우
    case_2 = len(str(n))
elif m != 10: # 버튼이 고장난 경우
    interval = 0
    while True:
        minus = n-interval if n-interval > 0 else 0
        plus = n+interval
        if len(buttons & set(str(minus))) == 0:
            case_2 = (interval + len(str(minus)))
            break
        if len(buttons & set(str(plus))) == 0:
            case_2 = (interval + len(str(plus)))
            break
        interval += 1

answer = min(case_1,case_2)
print(answer)
