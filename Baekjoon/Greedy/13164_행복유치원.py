import sys
input = sys.stdin.readline

N, K = map(int, input().split())
children = list(map(int, input().split()))
sub_height = sorted([children[c+1] - children[c] for c in range(len(children) - 1)])

print(sum(sub_height[:N-K]))