import numpy as np
cnt_0 = 0
cnt_1 = 0
def compress(arr):
    global cnt_0, cnt_1
    m = len(arr)//2
    arr = np.array(arr)
    arr1 = arr[0:m,0:m]
    arr2 = arr[0:m,m:]
    arr3 = arr[m:,0:m]
    arr4 = arr[m:,m:]

    s1 = set()
    for i in arr1:
        for j in i:
            s1.add(j)
    if len(s1)!=1:
        compress(arr1)
    else:
        if s1.pop() == 1:
            cnt_1 += 1
        else:
            cnt_0 += 1

    s2 = set()
    for i in arr2:
        for j in i:
            s2.add(j)
    if len(s2) != 1:
        compress(arr2)
    else:
        if s2.pop() == 1:
            cnt_1 += 1
        else:
            cnt_0 += 1

    s3 = set()
    for i in arr3:
        for j in i:
            s3.add(j)
    if len(s3) != 1:
        compress(arr3)
    else:
        if s3.pop() == 1:
            cnt_1 += 1
        else:
            cnt_0 += 1

    s4 = set()
    for i in arr4:
        for j in i:
            s4.add(j)
    if len(s4) != 1:
        compress(arr4)
    else:
        if s4.pop() == 1:
            cnt_1 += 1
        else:
            cnt_0 += 1

    return


def solution(arr):
    global cnt_0,cnt_1
    s = set()
    for i in arr:
        for j in i:
            s.add(j)
    if len(s)==1:
        if s.pop()==1:
            cnt_1+=1
        else:
            cnt_0+=1
        return [cnt_0,cnt_1]
    else:
        compress(arr)
    return [cnt_0,cnt_1]

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))