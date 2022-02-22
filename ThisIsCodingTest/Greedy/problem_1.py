# solution_1
# N, M, K = map(int, input().split())
# arr = list(map(int, input().split()))
#
# arr.sort()
# answer = 0
# for i in range(M):
# 	if i % (K + 1) == K:
# 		answer += arr[-2]
# 	else:
# 		answer += arr[-1]
# print(answer)

# solution_2
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
answer = 0
cnt = M // (K + 1)
answer = arr[-1] * (M - cnt) + arr[-2] * cnt
print(answer)