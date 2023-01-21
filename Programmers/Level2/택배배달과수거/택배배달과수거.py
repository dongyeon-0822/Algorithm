def solution(cap, n, deliveries, pickups):
    answer = 0

    delivery = n-1 # 수거 위치를 의미 하는 포인터
    pickup = n-1 # 수거 위치를 의미 하는 포인터
    while delivery >= 0 or pickup >= 0:
        distance = 0
        if delivery >= 0 :
            while delivery >= 0 and deliveries[delivery] == 0: # 옮길 택배가 있을 때까지
                delivery -= 1
            if delivery < 0: distance = 0
            else: distance = delivery+1 # 최대 거리 저장

            car = 0 # 트럭에 있는 택배 무게
            while delivery >= 0 and car < cap: # 현재 집에 택배를 트럭에 실을 수 있다면 싣는다.
                if deliveries[delivery] + car <= cap:
                    car += deliveries[delivery]
                    deliveries[delivery] = 0
                    delivery -= 1
                else:
                    rest = cap - car
                    deliveries[delivery] -= rest
                    break



        if pickup >= 0:
            while pickup >= 0 and pickups[pickup] == 0: # 옮길 택배가 있을 때까지
                pickup -= 1
            if pickup < 0: distance = 0
            else: distance = max(distance, pickup+1) # 최대 거리 저장


            car = 0 # 트럭에 있는 택배 무게
            while pickup >= 0 and car < cap: # 현재 집에 택배를 트럭에 실을 수 있다면 싣는다.
                if pickups[pickup] + car <= cap:
                    car += pickups[pickup]
                    pickups[pickup] = 0
                    pickup -= 1
                else:
                    rest = cap - car
                    pickups[pickup] -= rest
                    break

        answer += distance*2
    return answer

print(solution(2,2, [0,0], [0,0]))