def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck=[[0,x] for x in truck_weights]

    on_bridge=[]
    on_weight=0

    while not truck_weights.empty():
        answer+=1
        for i,j in on_bridge:



    return answer