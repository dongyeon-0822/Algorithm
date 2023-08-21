from collections import Counter

def solution(want, number, discount):
    answer = 0
    wants = dict(zip(want,number))
    for i in range(len(discount) - 10 + 1):
        if wants == Counter(discount[i:i + 10]):
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))