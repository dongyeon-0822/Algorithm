# https://www.acmicpc.net/problem/14888
# 순열을 이용한 풀이

import sys
from itertools import permutations
import math
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
idx_op = sum([[i]*o for i,o in enumerate(op)], [])

set_op = set(permutations(idx_op,N-1))
answers = []
for s in set_op:
    answer = A[0]
    for i,o in enumerate(s):
        if o == 0:
            answer += A[i+1]
        elif o == 1:
            answer -= A[i+1]
        elif o == 2:
            answer *= A[i+1]
        elif o == 3:
            tmp = answer / A[i+1]
            if tmp > 0:
                answer = math.floor(tmp)
            else:
                answer = math.ceil(tmp)
    answers.append(answer)
print(max(answers))
print(min(answers))