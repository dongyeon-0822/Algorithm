import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

answer = 0
if N == 1 or (N == 2 and arr[0] != arr[1]): # 값이 하나거나 다른 2개의 값인 경우
    answer = 'A'
elif N == 2 and arr[0] == arr[1]:
    answer = arr[0]
else:
    sub = [arr[i+1] - arr[i] for i in range(N-1)]
    if 0 in sub : # 0 일 때 : 같은 숫자가 연속으로 나올 때
        if all(i == 0 for i in sub[1:]):
            answer = arr[-1]
        else:
            answer = 'B'
    else:
        div = [sub[i+1]/sub[i] for i in range(len(sub)-1)]
        if len(set(div)) != 1 or div[0] != int(div[0]): # 규칙이 없는 경우 또는 정수가 아닌 경우
            answer = 'B'
        else:
            answer = arr[-1] + sub[-1]*int(div[0])
print(answer)
