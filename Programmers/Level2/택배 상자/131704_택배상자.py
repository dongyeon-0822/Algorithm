def solution(order):
    answer = []

    sub_container = []
    current_box = 1
    idx = 0
    while idx < len(order):
        while sub_container and order[idx] == sub_container[-1]: # 보조 컨테이너 확인
            answer.append(sub_container.pop())
            idx += 1
        while current_box <= len(order): # 메인 컨테이너 확인
            if order[idx] == current_box:
                answer.append(current_box)
                current_box += 1
                idx += 1
                break
            sub_container.append(current_box)
            current_box += 1
        else:
            break

    return len(answer)

solution([4, 3, 1, 2, 5])