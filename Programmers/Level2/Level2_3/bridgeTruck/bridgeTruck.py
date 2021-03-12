def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck=[[0,x] for x in truck_weights]

    on_bridge=[]
    on_weight=0
    while len(truck):
        if on_weight+truck[0][1]<=weight:
            on_weight+=truck[0][1]
            on_bridge.append(truck[0])
            del truck[0]
        for i in on_bridge:
            i[0]+=1
        for i in on_bridge:
            if i[0] == bridge_length:
                on_weight -= i[1]
                del on_bridge[0]
        answer+=1
    return answer+bridge_length

if __name__=='__main__':
    print(solution(2,10,[7,4,5,6]))