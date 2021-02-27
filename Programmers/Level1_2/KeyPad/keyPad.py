def compare(loc_L,loc_R,loc,h):
    if loc_L=='*': loc_L=10
    if loc==0: loc=11
    if loc_R==0: loc_R=11
    if loc_L==0: loc_L=11
    if loc_R=='#': loc_R=12

    pad=[(i, j) for i in range(4) for j in range(3)]
    dis_L=abs(pad[loc_L-1][0]-pad[loc-1][0])+abs(pad[loc_L-1][1]-pad[loc-1][1])
    dis_R = abs(pad[loc_R- 1][0] - pad[loc - 1][0]) + abs(pad[loc_R - 1][1] - pad[loc-1][1])
    if dis_L<dis_R: return 'L'
    elif dis_L>dis_R: return 'R'
    else: return h

def solution(numbers, hand):
    answer = ''
    loc_L='*'
    loc_R='#'
    if hand=='right': h='R'
    else: h='L'
    for i in numbers:
        if i in [1,4,7]:
            answer+='L'
            loc_L=i
        elif i in [3,6,9]:
            answer+='R'
            loc_R=i
        elif i in [2,5,8,0]:
            com=compare(loc_L,loc_R,i,h)
            answer+=com
            if com=='R': loc_R=i
            else: loc_L=i
    return answer

if __name__=='__main__':
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
