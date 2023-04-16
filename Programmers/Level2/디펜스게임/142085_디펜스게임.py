import heapq

def solution(n, k, enemy):
    answer = 0
    soldier = []

    for e in enemy:
        if n-e >= 0: # 병사로 막을 수 있으면 막기
            n -= e
            heapq.heappush(soldier, -e)
            answer += 1
        elif k > 0: # 무적권 사용
            if len(soldier) != 0 and abs(soldier[0]) > e:
                n += abs(heapq.heappop(soldier))
                n -= e
                heapq.heappush(soldier, -e)
            k -= 1
            answer += 1
        else: break

    return answer