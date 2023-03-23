def solution(X, Y):
    answer = ''
    x_arr = [0]*10
    y_arr = [0]*10

    for x in X:
        x_arr[int(x)] += 1
    for y in Y:
        y_arr[int(y)] += 1

    nums = []
    for i,(x,y) in enumerate(zip(x_arr, y_arr)):
        for _ in range(min(x,y)):
            nums.append(str(i))

    nums = "".join(sorted(nums, reverse=True))

    if len(nums) == 0:
        answer = "-1"
    elif nums[0] == '0':
        answer = "0"
    else:
        answer = nums

    return answer
