N = int(input())
arr = []
for i in range(N):
    S = input()
    arr.append(S)
arr = list(set(arr))
arr.sort(key=lambda x : (len(x), x))
for s in arr:
    print(s)