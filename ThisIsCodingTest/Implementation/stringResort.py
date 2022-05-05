S = input()

arr = []
count = 0
for s in S:
    if s.isalpha():
        arr.append(s)
    else:
        count += int(s)
answer = "".join(sorted(arr))
print(answer+str(count))