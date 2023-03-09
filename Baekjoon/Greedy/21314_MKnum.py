import sys
input = sys.stdin.readline

s = input().rstrip();

max_num = ""
min_num = ""

n = 0
for x in s:
    if x == "M":
        n += 1
    else:
        if n > 0:
            max_num += "5" + "0" * n
            min_num += str(10 ** (n-1)) + "5"
        else:
            max_num += "5"
            min_num += "5"
        n = 0
if n > 0:
    max_num += "1" * n
    min_num += str(10 ** (n-1))

print(max_num)
print(min_num)