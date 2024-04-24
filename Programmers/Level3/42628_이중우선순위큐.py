import heapq


def solution(operations):
    answer = [0, 0]
    heap = [] # 최소 힙

    for operation in operations:
        cmd, num = operation.split()
        if cmd == 'I': # 숫자 삽입
            heapq.heappush(heap, int(num))
        elif heap and int(num) > 0: # 최댓값 삭제
            heap = heapq.nsmallest(len(heap)-1, heap)
            heapq.heapify(heap)
        elif heap and int(num) < 0: # 최솟값 삭제
            heapq.heappop(heap)

    if heap:
        min_v = heap[0]
        max_v = heapq.nlargest(1, heap)[0]
        answer = [max_v, min_v]
    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))