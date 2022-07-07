# https://www.acmicpc.net/problem/18310
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[(N-1)//2])

# 시간초과,,,
# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# inter = [arr[i+1] - arr[i] for i in range(N-1)]
#
# answer = []
# for i in range(N):
#     tmp = [sum(inter[x:i]) for x in range(i)]
#     tmp.extend([sum(inter[i:i+x]) for x in range(1,N-i)])
#     answer.append(sum(tmp))
#
# print(arr[answer.index(min(answer))])