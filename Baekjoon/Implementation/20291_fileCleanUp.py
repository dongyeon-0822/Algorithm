import sys
input = sys.stdin.readline

N = int(input())
files = {}
for _ in range(N):
    file = input().strip().split('.')[1]
    if file in files:
        files[file] += 1
    else:
        files[file] = 1

for f in sorted(list(files.keys())):
    print(f, files[f])