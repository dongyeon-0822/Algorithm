N, K = map(int, input().split())

answer = 0
while N > 1:
	if N % K == 0:
		answer += 1
		N /= K
	else:
		answer += int(N % K)
		N -= (N % K)
		if N == 0:
			answer -= 1
print(answer)