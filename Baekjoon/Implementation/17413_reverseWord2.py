import sys
input = sys.stdin.readline

answer = []
string = input().strip()
word = []
tmp = ""
for s in string:
    if s == '<':
        if tmp != "":
            word.append(tmp)
        tmp = ""
        tmp += s
    elif s == '>':
        tmp += s
        word.append(tmp)
        tmp = ""
    else:
        tmp += s
if tmp != "":
    word.append(tmp)

for w in word:
    if w[0] == '<':
        answer.append(w)
    else:
        tmp = w.split()
        tmp = [s[::-1] for s in tmp]
        answer.append(' '.join(tmp))

print(''.join(answer))