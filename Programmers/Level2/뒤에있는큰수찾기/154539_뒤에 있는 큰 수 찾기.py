def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [[-1, int(1e6)]]

    for i, number in enumerate(numbers):
        while stack[-1][1] < number:
            answer[stack.pop()[0]] = number
        stack.append([i, number])

    return answer

print(solution([9, 1, 5, 3, 6, 2]))
