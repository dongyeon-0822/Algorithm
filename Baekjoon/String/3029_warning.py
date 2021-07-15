if __name__ == '__main__':
    now_time = list(map(int,input().split(':')))
    bomb_time = list(map(int,input().split(':')))

    sec = bomb_time[-1] - now_time[-1]
    if sec<0:
        sec=sec+60
        if bomb_time[1]<=0:
            bomb_time[0]-=1
            bomb_time[1]+=60
        bomb_time[1]-=1

    min = bomb_time[1] - now_time[1]
    if min<0:
        min=min+60
        bomb_time[0]-=1

    hour = bomb_time[0] - now_time[0]
    if hour<0:
        hour=hour+24

    if hour==min==sec==0:
        hour+=24
    hour = str(hour).zfill(2)
    min = str(min).zfill(2)
    sec = str(sec).zfill(2)

    print(hour+':'+min+':'+sec)