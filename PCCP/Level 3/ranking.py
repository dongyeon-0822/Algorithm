def solution(n, results):
    answer = 0

    arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for x,y in results:
        arr[x][y] = 1
        arr[y][x] = -1

    for k in range(1, n+1):
        for i in range(1,n+1):
            for j in range(1, n+1):
                if arr[i][j] == 0 and arr[i][k] == arr[k][j] == 1:
                    arr[i][j] = 1
                elif arr[i][j] == 0 and arr[i][k] == arr[k][j] == -1:
                    arr[i][j] = -1
    for row in arr[1:]:
        # print(row)
        if row[1:].count(0) == 1:
            answer+=1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)