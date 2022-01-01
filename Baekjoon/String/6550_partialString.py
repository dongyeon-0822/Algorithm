#반례 모르겠음
s,t = input().split()

result = True
idx = 0
if set(s)&set(t) != set(s):
    result = False
else:
    for i in s:
        if i not in t[idx:]:
            result = False
        else:
            idx += t[idx:].index(i)

if result:
    print('Yes')
else:
    print('No')
