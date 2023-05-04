# split. join -> 30%
# replace -> 4개 시간 초과
# find, indexing -> 2개 시간 초과

def solution(ingredient):
    answer = 0

    hamburger = [1,2,3,1]
    i = 0
    while len(ingredient) >= 4 and i <= len(ingredient) - 4:
        if ingredient[i:i+4] == hamburger:
            answer += 1
            del ingredient[i:i+4]
            i = i-4 if i-4 >= 0 else -1
        i += 1

    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
