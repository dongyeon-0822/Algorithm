def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    idx_a, idx_b = 0, 0
    while idx_a < len(A) and idx_b < len(B):
        if A[idx_a] < B[idx_b]:
            answer += 1
            idx_a += 1
        idx_b += 1
    return answer