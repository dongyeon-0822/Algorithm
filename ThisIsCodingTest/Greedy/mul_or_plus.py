str = input()

answer = int(str[0])
for i in range(1, len(str)):
    if int(answer) <= 1 or int(str[i]) <= 1:
        answer += int(str[i])
    else:
        answer *= int(str[i])
print(answer)