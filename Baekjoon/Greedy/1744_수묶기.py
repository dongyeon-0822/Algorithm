import sys
input = sys.stdin.readline

answer = 0
N = int(input())
minus_nums = []
plus_nums = []
for _ in range(N):
    num = int(input())
    if num <= 0:
        minus_nums.append(num)
    else:
        plus_nums.append(num)

minus_nums.sort()
plus_nums.sort(reverse=True)

tmp = 0
for i, num in enumerate(minus_nums):
    if i % 2 == 0:
        tmp = num
        if i == len(minus_nums)-1:
            answer += tmp
    else:
        if tmp * num > tmp + num:
            tmp *= num
        else:
            tmp += num
        answer += tmp

tmp = 0
for i, num in enumerate(plus_nums):
    if i % 2 == 0:
        tmp = num
        if i == len(plus_nums)-1:
            answer += tmp
    else:
        if tmp * num > tmp + num:
            tmp *= num
        else:
            tmp += num
        answer += tmp
print(answer)