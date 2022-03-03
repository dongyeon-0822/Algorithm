import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
dic = {}
for i in range(N):
    dic[i+1] = input().rstrip()
reverse_dict= dict(map(reversed,dic.items()))
for i in range(M):
    read = input().rstrip()
    if read.isdigit():
        print(dic[int(read)])
    else:
        print(reverse_dict[read])