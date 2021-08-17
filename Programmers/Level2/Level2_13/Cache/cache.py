def solution(cacheSize, cities):
    answer = 0
    cache = []
    for c in [x.upper() for x in cities]:
        if c not in cache:
            answer+=5
            if len(cache)<cacheSize:
                cache.append(c)
            else:
                cache.append(c)
                cache.pop(0)
        else:
            answer+=1
            cache.pop(cache.index(c))
            cache.append(c)

    return answer