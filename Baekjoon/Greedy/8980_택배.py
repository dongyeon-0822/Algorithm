import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

# 마을의 개수, 트럭의 용량, 박스 정보(보내는 마을번호, 받는 마을번호, 박스 개수)
# 조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
# 조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
# 조건 3: 박스들 중 일부만 배송할 수도 있다.

N, C = map(int, input().split())
M = int(input())
boxs = defaultdict(list) # {보내는 마을: [받는 마을, 박스의 개수]}
for _ in range(M):
    send, receive, box = map(int, input().split())
    boxs[send].append([receive, box])

answer = 0
weight = C
trucks = [0] * (N+1) # 마을에 보내는 택배 개수
trucks_key = [] # 최대 힙 : 받는 마을 번호
for n in range(1, N+1): # 마을 번호 순회
    # 내리기
    answer += trucks[n]
    weight += trucks[n]
    trucks[n] = 0
    # 올리기
    for receive, box in boxs[n]:
        if trucks[receive] == 0:
            heapq.heappush(trucks_key, -receive)
        trucks[receive] += box
        weight -= box
    while weight < 0:
        max_receive = -trucks_key[0]
        if -weight >= trucks[max_receive]: # 초과 무게 >= 내릴 무게
            weight += trucks[max_receive]
            trucks[max_receive] = 0
            heapq.heappop(trucks_key)
        else: # 초과 무게 < 내릴 무게
            trucks[max_receive] += weight
            weight = 0
print(answer)
