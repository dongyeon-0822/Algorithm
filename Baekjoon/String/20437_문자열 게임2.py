import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answers = []
    W = input().rstrip()
    K = int(input())
    alpha = defaultdict(list)

    # 각 알파벳 딕셔너리에 인덱스 저장
    for i, w in enumerate(W):
        alpha[w].append(i)

    # K개 이상인 알파벳에 대해 정렬 후 k만큼 슬라이싱 짧은 문자열, 긴 문자열 찾기
    for k, v in alpha.items():
        if len(v) < K: continue
        v.sort()
        for i in range(len(v)-K+1):
            answers.append(v[i+K-1]-v[i]+1)

    if answers:
        print(min(answers), max(answers))
    else:
        print(-1)
