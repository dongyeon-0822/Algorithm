import sys
from itertools import combinations
input = sys.stdin.readline

def is_fit(long, short, sticker1, sticker2):
    # 기본 조건 만족 시
    if sticker1[1] <= long and sticker2[1] <= long \
        and sticker1[0] <= short and sticker2[0] <= short \
        and sticker1[2] + sticker2[2] <= long * short:
        if sticker1[1] <= short: # 큰 스티커 긴 부분이 짧은 변에 들어갈 때
            s = short - sticker1[1]
            l = long - sticker1[0]
            if (sticker2[0] <= l and sticker2[1] <= short) \
                or (sticker2[0] <= short and sticker2[1] <= l) \
                or (sticker2[0] <= s and sticker2[1] <= long) \
                or (sticker2[0] <= long and sticker2[1] <= s):
                area = sticker1[2] + sticker2[2]
                return area
        else: # 큰 스티커의 짧은 부분은 긴 변에 들어갈 때
            s = short - sticker1[0]
            l = long - sticker1[1]
            if (sticker2[0] <= l and sticker2[1] <= short) \
                or (sticker2[0] <= short and sticker2[1] <= l) \
                or (sticker2[0] <= s and sticker2[1] <= long) \
                or (sticker2[0] <= long and sticker2[1] <= s):
                area = sticker1[2] + sticker2[2]
                return area
    return 0

arr = list(map(int, input().split()))
arr.sort()
H, W = arr[0], arr[1]
N = int(input())
sticker = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp.sort()
    tmp.append(tmp[0] * tmp[1])
    sticker.append(tmp)

sticker.sort(key=lambda x:-x[2])
comb_stickers = list(combinations(sticker, 2))

answer = []
if N == 1:
    answer.append(0)
for stickers in comb_stickers:
    answer.append(is_fit(W, H, stickers[0], stickers[1]))
    answer.append(is_fit(W, H, stickers[1], stickers[0]))

print(max(answer))
