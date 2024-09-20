import sys
input = sys.stdin.readline

n = int(input())
graph = {}
for _ in range(n):
    a, b = input().rstrip().split(" is ")
    graph[a] = b

m = int(input())
for _ in range(m):
    a, b = input().rstrip().split(" is ")
    node = a
    while node in graph:
        node = graph[node]
        if node == b:
            print("T")
            break
    else:
        print("F")