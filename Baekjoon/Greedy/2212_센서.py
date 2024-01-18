import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))
inter = sorted([sensor[i+1] - sensor[i] for i in range(len(sensor) - 1)])
print(sum(inter[:len(inter)-(K-1)]))