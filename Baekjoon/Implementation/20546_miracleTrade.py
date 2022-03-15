import sys
input = sys.stdin.readline

money = int(input())
stock = list(map(int, input().split()))

a_money = money
a_stock = 0
for s in stock:
    a_stock = a_money / s
    a_money %= s
a_total = a_money + stock[-1] * a_stock

b_count = 0
b_flag = 0
b_temp = 0
for s in stock:
    if b_flag == 0:
        b_temp = s
    if b_temp < s:
        b_flag = -1
        b_temp = s
        b_count += 1
    elif b_temp > s:
        b_flag = 1
        b_temp = s
        b_count += 1
    if b_count >= 3:
        a_stock = a_money / s
        a_money %= s
