s,t = input().split()

idx = []
result = True
for i in s:
    if i in t:
        idx.append(t.index(i))
    else:
        result = False
if idx != sorted(idx):
    result = False

if result:
    print('Yes')
else:
    print('No')
