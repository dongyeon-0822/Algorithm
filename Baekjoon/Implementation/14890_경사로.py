import sys
input = sys.stdin.readline

N, L = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(N)]

answer = 0
def find_road(arr):
    cnt = 0
    for line in arr: # 가로 행 검사
        flag = [True] * N
        i = 1
        while i < N:
            if line[i-1] - line[i] == 1: # 내려가는 경우
                if i + L <= N and all(flag[i:i+L]) and len(set(line[i:i+L])) == 1:
                    for idx in range(i, i+L):
                        flag[idx] = False
                    i += L
                else: break
            elif line[i] - line[i-1] == 1: # 올라가는 경우
                if i - L >= 0 and all(flag[i-L:i]) and len(set(line[i-L:i])) == 1:
                    for idx in range(i-L, i):
                        flag[idx] = False
                    i += 1
                else: break
            elif line[i] == line[i-1]: # 같은 경우
                i += 1
            else: break
        else:
            cnt += 1
    return cnt

answer += find_road(roads)
answer += find_road(zip(*roads))
print(answer)

