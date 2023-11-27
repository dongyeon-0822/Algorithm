def solution(bandage, health, attacks):
    t, x, y = bandage
    ex_time = 0
    exp = health
    for time, amount in attacks:
        d = time - ex_time - 1
        exp += d * x + (d // t) * y
        exp = health if exp >= health else exp
        exp -= amount
        ex_time = time
        if exp <= 0: return -1
    return exp

print(solution(	[3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))