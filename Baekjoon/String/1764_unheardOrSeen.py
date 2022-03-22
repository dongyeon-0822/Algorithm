N, M = map(int, input().split())
heard = []
seen = []
for i in range(N):
    heard.append(input())
for i in range(M):
    seen.append(input())
heardSeen = list(set(heard) & set(seen))
heardSeen.sort()
print(len(heardSeen))
for i in heardSeen:
    print(i)