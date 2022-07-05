import sys
input = sys.stdin.readline

sound = input().rstrip()
correct = ['q','u','a','c','k']
ducks = [[]]
cnt = 1
i = 0
flag = False
for s in sound:
    for d in ducks:
        exist = False
        if len(d) == correct.index(s):
            exist = True
            d.append(s)
            if len(d) == 5:
                d.clear()
            break
    if not exist:
        if s == 'q':
            ducks.append(['q'])
            cnt += 1
        else:
            flag = True
            break
    if flag:
        break

for d in ducks:
    if len(d) != 0:
        flag = True
        break
if flag:
    print(-1)
else:
    print(cnt)