N = int(input())
x, y = 1, 1
plans = input().split()

for plan in plans:
    if plan == 'L' and y > 1:
        y -= 1
    elif plan == 'R' and y < N:
        y += 1
    elif plan == 'U' and x > 1:
        x -= 1
    elif plan == 'D' and x < N:
        x += 1

print(x,y)

##### answer #####
# for plan in plans:
#     for i in range(len(move_type)):
#         if plan == move_type[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx <1 or ny < 1 or nx > N or ny > N:
#         continue
#     x, y = nx, ny