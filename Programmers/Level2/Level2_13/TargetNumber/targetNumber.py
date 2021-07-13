arr=[]
def dfs(numbers, target, result, count, sign):
    if sign: result += numbers[count]
    else: result -= numbers[count]
    count += 1
    if count == len(numbers):
        if result==target:
            arr.append(1)
        return
    else:
        dfs(numbers, target, result, count, 1)
        dfs(numbers, target, result, count, 0)

def solution(numbers, target):
    result = 0
    count = 0
    dfs(numbers, target, result, count, 1)
    dfs(numbers, target, result, count, 0)
    return len(arr)

if __name__ == '__main__':
    solution([1,1,1,1,1],3)