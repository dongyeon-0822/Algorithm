import sys
input = sys.stdin.readline

N = int(input())
option = [list(input().split()) for _ in range(N)]
keys = []
answer = []

for o in option:
    flag = False
    first = [x[0] for x in o]
    for i, f in enumerate(first):
        if f.upper() in keys:
            continue
        else:
            o[i] = "["+f+"]"+o[i][1:]
            answer.append(" ".join(o))
            keys.append(f.upper())
            flag = True
            break
    if not flag:
        for i, word in enumerate(o):
            for j,s in enumerate(word):
                if s.upper() in keys:
                    continue
                else:
                    o[i] = word[:j] + "[" + s + "]" + word[j+1:]
                    answer.append(" ".join(o))
                    keys.append(s.upper())
                    flag = True
                    break
            if flag:
                break
    if not flag:
        answer.append(" ".join(o))
for a in answer:
    print(a)