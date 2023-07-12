def solution(elements):
    answer = 0
    result = []
    long_elements = elements + elements
    for i in range(len(elements)):
        for j in range(len(elements)):
            result.append(sum(long_elements[j:j+i]))
    result = list(set(result))
    answer = len(result)
    return answer