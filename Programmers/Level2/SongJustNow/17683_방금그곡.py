def solution(m, musicinfos):
    answer = ''
    infos = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    for music in musicinfos:
        start, end, title, info = music.split(',')
        sec = (int(end[0:2]) - int(start[0:2])) * 60 + (int(end[3:]) - int(start[3:]))
        info = info.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        info = (info * (sec//len(info)+1))[0:sec]
        if m in info:
            infos.append([sec, info, title])

    if len(infos) == 1: # 조건 일치 1개
        return infos[0][2]
    elif len(infos) == 0: # 조건 일치 X
        return '(None)'
    else: # 조건 일치 여러 개
        arr = sorted(infos, key=lambda x:-x[0])
        return arr[0][2]

solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])