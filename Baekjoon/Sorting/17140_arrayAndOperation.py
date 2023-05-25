import sys
input = sys.stdin.readline

r,c,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

count = 0
while True:
    if (r-1 < len(arr) and c-1 < len(arr[0])) and (arr[r-1][c-1] == k):
        break
    count += 1
    if count > 100:
        break

    r_num = len(arr)
    c_num = len(arr[0])

    arr_tmp = []
    if r_num < c_num:
        arr = list(zip(*arr))
    for row in arr:
        s = list(set(row))
        middle = [[x,row.count(x)] for x in s if x != 0]
        result = sum(sorted(middle, key=lambda x : (x[1], x[0])),[])
        arr_tmp.append(result)
    max_len = max([len(row) for row in arr_tmp])
    for i in range(len(arr_tmp)):
        zero = [0] * (max_len-len(arr_tmp[i]))
        arr_tmp[i] += zero
    if r_num >= c_num:
        arr = arr_tmp
    else:
        arr = list(map(list, list(zip(*arr_tmp))))

if count > 100:
    print(-1)
else:
    print(count)