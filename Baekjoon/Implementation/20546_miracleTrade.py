import sys
input = sys.stdin.readline

money = int(input())
stock = list(map(int, input().split()))

a_money = money
a_stock = 0
for s in stock:
    a_stock += a_money // s
    a_money %= s
a_total = a_money + stock[-1] * a_stock

b_money = money
b_stock = 0
b_count = 0
b_flag = 0
b_temp = 0
for i,s in enumerate(stock):
    if i == 0:
        b_temp = s
        continue
    if b_temp < s:
        if b_flag <= 0:
            b_count += 1
        elif b_flag > 0:
            b_count = 1
        b_flag = -1
    elif b_temp > s:
        if b_flag >= 0:
            b_count += 1
        elif b_flag < 0:
            b_count = 1
        b_flag = 1
    b_temp = s
    if b_count >= 3 and b_flag > 0:
        b_stock += b_money // s
        b_money %= s
    elif b_count >= 3 and b_flag < 0:
        b_money += b_stock * s
        b_stock = 0
b_total = b_money + stock[-1] * b_stock

if a_total > b_total:
    print("BNP")
elif a_total < b_total:
    print("TIMING")
else:
    print("SAMESAME")