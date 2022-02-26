S = input()

cnt_0 = 0
cnt_1 = 0
tmp = S[0]
if tmp == '0':
    cnt_0 += 1
else:
    cnt_1 += 1
for i in range(1, len(S)):
    if S[i] != tmp:
        if S[i] == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1
        tmp = S[i]
print(min(cnt_0,cnt_1))