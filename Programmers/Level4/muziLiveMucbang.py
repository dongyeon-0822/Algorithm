# 효율성 통과 X
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    n = len(food_times)
    idx = 0
    while k >= 0:
        if food_times[idx % n] > 0:
            food_times[idx % n] -= 1
            k -= 1
        idx += 1
    return (idx-1) % n + 1

if __name__ == '__main__':
    print(solution([3,1,1,1,2,4,3],12))