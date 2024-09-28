arr = list(input())
N = len(arr)
left_bracket = 0
right_bracket = 0
balance_bracket = 0
answer = 0

for i in range(N):
    if arr[i] == '(':
        left_bracket += 1
        balance_bracket += 1
    else:
        right_bracket += 1
        balance_bracket -= 1

    if balance_bracket <= 1:
        left_bracket = 0

    if balance_bracket == -1:
        answer = right_bracket
        break


if balance_bracket > 0:
    answer = left_bracket
print(answer)