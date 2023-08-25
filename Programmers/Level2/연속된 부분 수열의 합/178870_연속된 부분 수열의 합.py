def solution(sequence, k):
    answer = []

    part_sum = 0
    start_idx = 0
    for i, n in enumerate(sequence):
        part_sum += n
        while part_sum > k:
            part_sum -= sequence[start_idx]
            start_idx += 1
        if part_sum == k:
            answer.append([start_idx, i])
    answer.sort(key= lambda x : (x[1] - x[0], x[0]))
    return answer[0]

print(solution(	[1, 1, 1, 2, 3, 4, 5], 5))