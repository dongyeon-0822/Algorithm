def solution(n):
    arr = []
    for i in range(1,n):
        if (n-1) % i == 0:
            arr.append(i)
    return arr[1]
print(solution(10))