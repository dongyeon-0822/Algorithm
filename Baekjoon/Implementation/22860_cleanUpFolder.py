import sys
input = sys.stdin.readline

def searchDic(dic, file, name):
    for x in dic[name]:
        if x[1] == '0':
            file.append(x[0])
        else:
            searchDic(dic, file, x[0])
    return

directory = {}

N, M = map(int, input().split())
for _ in range(N+M):
    tmp = input().split()
    if tmp[0] in directory:
        directory[tmp[0]].append([tmp[1], tmp[2]])
    else:
        directory[tmp[0]] = [[tmp[1], tmp[2]]]
    if tmp[2]=='1' and tmp[1] not in directory:
        directory[tmp[1]] = []

Q = int(input())
queries = [input().rstrip().split('/') for _ in range(Q)]

for query in queries:
    files = []
    for x in directory[query[-1]]:
        if x[1] == '0':
            files.append(x[0])
        else:
            searchDic(directory, files, x[0])
    print(len(set(files)), len(files))
