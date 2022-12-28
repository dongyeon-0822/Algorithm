import sys
input = sys.stdin.readline

# 바로 앞 문자와 같은지 체크
def dfs(pre_char, length):
    global total
    if length == len(s):
        total += 1
        return

    for key in dic.keys():
        if pre_char != key and dic[key] != 0:
            dic[key] -= 1
            dfs(key, length + 1)
            dic[key] += 1 # 다시 되돌려 주기


s = input().rstrip()
dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

total = 0
dfs("", 0)
print(total)