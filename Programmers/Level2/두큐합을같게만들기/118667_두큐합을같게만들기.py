from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    limit = len(queue1) + len(queue2) + 2

    if (sum1 + sum2) % 2 == 1:
        return - 1
    answer = 0
    while sum1 != sum2:
        while sum1 > sum2 and queue1:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            answer += 1
        while sum1 < sum2 and queue2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            answer += 1
        if answer > limit:
            return -1
    return answer
print(solution([3, 3, 3, 3], [3, 3, 21, 3]))