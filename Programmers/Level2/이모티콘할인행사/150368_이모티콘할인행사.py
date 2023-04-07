from itertools import product

def solution(users, emoticons):
    sales = list(product([10, 20, 30, 40], repeat = len(emoticons)))

    result = []
    for sale in sales:
        join, profit = 0, 0
        for rate, price in users:
            consume = 0
            for s, emoticon in zip(sale, emoticons):
                if s >= rate:
                    consume += emoticon * (1 - s * 0.01)
            if consume >= price:
                join += 1
            else:
                profit += consume
        result.append([join, profit])

    result.sort(key = lambda x:(-x[0],-x[1]))
    return result[0]
