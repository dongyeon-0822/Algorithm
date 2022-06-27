import sys
input = sys.stdin.readline

sound = input().rstrip()
ducks = [[]]
n = 1
flag = False
for s in sound:
    if s == 'q':
        exist = False
        for d in ducks:
            if len(d) == 0:
                exist = True
                d.append('q')
                break
        if not exist:
            ducks.append(['q'])
            n += 1
    elif s == 'u':
        exist = False
        for d in ducks:
            if len(d) == 1:
                exist = True
                d.append('u')
                break
        if not exist:
            flag = True
            break
    elif s == 'a':
        exist = False
        for d in ducks:
            if len(d) == 2:
                exist = True
                d.append('a')
                break
        if not exist:
            flag = True
            break
    elif s == 'c':
        exist = False
        for d in ducks:
            if len(d) == 3:
                exist = True
                d.append('c')
                break
        if not exist:
            flag = True
            break
    elif s == 'k':
        exist = False
        for d in ducks:
            if len(d) == 4:
                exist = True
                d.append('k')
                d.clear()
                break
        if not exist:
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
    print(n)