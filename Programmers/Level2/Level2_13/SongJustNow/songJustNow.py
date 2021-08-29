def solution(m, musicinfos):
    answer = ''
    infos = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    for music in musicinfos:
        start,end,title,info = music.split(',')
        sec = (int(end[0:2])-int(start[0:2]))*60 + (int(end[3:])-int(start[3:]))
        info = info.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        info = info*(sec//len(info)+1)
        info = info[0:sec]
        if m in info:
            infos.append([sec,info,title])
    if len(infos)==0:
        return '(None)'
    elif len(infos)==1:
        return infos[0][2]
    else:
        arr=sorted(infos, key=lambda x:-x[0])
        return arr[0][2]

solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])