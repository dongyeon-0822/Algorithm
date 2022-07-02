import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식개수

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    result = sorted(q,key= lambda x:x[1])
    return result[(k-sum_value) % length][1]

# 효율성 통과 X 코드
# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#     n = len(food_times)
#     idx = 0
#     while k >= 0:
#         if food_times[idx % n] > 0:
#             food_times[idx % n] -= 1
#             k -= 1
#         idx += 1
#     return (idx-1) % n + 1