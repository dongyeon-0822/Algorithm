import sys
input = sys.stdin.readline

def print_arr(arr):
    for row in arr:
        for x in row:
            print(x, end=" ")
        print()

def rorate_arr(operator, arr):
    tmp_arr = []
    arr_col = list(map(list, zip(*arr)))

    if operator == 1:
        return arr[::-1]
    elif operator == 2:
        for a in arr:
            tmp_arr.append(a[::-1])
        return tmp_arr
    elif operator == 3:
        for a in arr_col:
            tmp_arr.append(a[::-1])
        return tmp_arr
    elif operator == 4:
        return arr_col[::-1]
    else:
        parts = [[] for _ in range(4)]
        for part_12, part_34 in zip(arr[:len(arr) // 2], arr[len(arr) // 2:]):
            parts[0].append(part_12[:len(arr[0]) // 2])
            parts[1].append(part_12[len(arr[0]) // 2:])
            parts[2].append(part_34[len(arr[0]) // 2:])
            parts[3].append(part_34[:len(arr[0]) // 2])
        if operator == 5:
            for a,b in zip(parts[3], parts[0]):
                tmp_arr.append(a + b)
            for c,d in zip(parts[2], parts[1]):
                tmp_arr.append(c + d)
        else:
            for a, b in zip(parts[1], parts[2]):
                tmp_arr.append(a + b)
            for c, d in zip(parts[0], parts[3]):
                tmp_arr.append(c + d)
        return tmp_arr


N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
operators = list(map(int, input().split()))

for op in operators:
    A = rorate_arr(op, A)
print_arr(A)