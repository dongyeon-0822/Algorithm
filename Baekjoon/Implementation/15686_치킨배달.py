import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
chickens = []
houses = []
answer = []
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j, x in enumerate(tmp):
        if x == 1: # 집의 좌표값 저장
            houses.append((i,j))
        if x == 2: # 치킨집이라면 좌표값 저장
            chickens.append((i,j))

# m개 선택한 치킨집만 존재하도록 graph 설정
graph_tmp = []
distance_tmp = []
for chicken in list(combinations(chickens, M)):
    chicken_distance = 0
    distance = []
    for house in houses:
        distance = [abs(house[0] - i) + abs(house[1] - j) for i,j in chicken]
        chicken_distance += min(distance)
    answer.append(chicken_distance)

print(min(answer))