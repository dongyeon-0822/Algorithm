from collections import deque, Counter

N = int(input())
answer = []
for _ in range(N):
    n = int(input())
    stuff = list(map(int, input().split()))
    cost = 0

    sale_stack = []
    stuff = deque(sorted(stuff, reverse=True))

    while stuff:
        sale_stack.append(stuff.popleft())
        for x in stuff:
            if sale_stack[-1] > x:
                sale_stack.append(x)
                stuff.remove(x)
                break
        cost += sale_stack[0]
        sale_stack = []
    answer.append(cost)

for i, a in enumerate(answer, 1):
    print("#" + str(i), a)

    # stuff_count = Counter(stuff)
    # stuff_keys = sorted(stuff_count.keys(), reverse=True)
    # sale = [] # 1+1
    #
    # while n: # 물건이 없어질 때까지
    #     for k in stuff_keys: # 비싼 물건 순으로
    #         if stuff_count[k] == 0: continue
    #         if len(sale) == 0 or (len(sale) == 1 and sale[0] > k):
    #             sale.append(k)
    #             stuff_count[k] -= 1
    #             n -= 1
    #         if len(sale) == 2:
    #             cost += sale[0]
    #             sale = []
    #             break
    #     else:
    #         if len(sale) == 1:
    #             cost += sale[0]
    #             sale = []
    # answer.append(cost)




