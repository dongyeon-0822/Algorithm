R, C, Q= map(int, input().split())
brightness = [list(map(int, input().split())) for _ in range(R)]
prefix_sum = [[0] * (C + 1)] +  [[0] + row[:] for row in brightness]

for i in range(1, R+1):
    for j in range(1, C+1):
        prefix_sum[i][j] = prefix_sum[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    num = (r2 - r1 + 1) * (c2 - c1 + 1)
    total = prefix_sum[r2][c2] - prefix_sum[r1-1][c2] - prefix_sum[r2][c1-1] + prefix_sum[r1-1][c1-1]
    print(total // num)
