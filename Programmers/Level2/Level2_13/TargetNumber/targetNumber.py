answer = 0
def dfs(numbers, target, result, count, answer, sign):
    if sign: result += numbers[count]
    else: result -= numbers[count]
    count += 1
    if count == len(numbers):
        if result==target:
            answer+=1
        return
    else:
        dfs(numbers, target, result, count, answer, 1)
        dfs(numbers, target, result, count, answer, 0)

def solution(numbers, target):
    global answer
    result = 0
    count = 0
    dfs(numbers, target, result, count, answer, 1)
    dfs(numbers, target, result, count, answer, 0)
    return answer

if __name__ == '__main__':
    solution([1,1,1,1,1],3)