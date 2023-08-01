from collections import Counter, defaultdict

def solution(topping):
    answer = 0

    dic_A = defaultdict(int)
    dic_B = Counter(topping)
    for t in topping:
        dic_A[t] += 1
        dic_B[t] -= 1
        if dic_B[t] == 0:
            del dic_B[t]
        if len(dic_A) == len(dic_B):
            answer += 1
    return answer

solution([1, 2, 3, 1, 4])