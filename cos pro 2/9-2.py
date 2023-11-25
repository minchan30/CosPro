def mmdd_to_dd(day) :
    mm, dd = day.split('/')
    return int(dd)

def solution(today, shelf_life, n, m) :
    answer = []
    today_dd = mmdd_to_dd(today)
    for product in shelf_life :
        product_dd = mmdd_to_dd(product)
        if today_dd + m < product_dd < today_dd + n:
            answer.append(0)
        elif today_dd <= product_dd < today_dd + m:
            answer.append(1)
        elif product_dd <= today_dd:
            answer.append(2)
    return answer

today = "09/15"
shelf_life = ["09/21", "09/16", "09/14"]
n = 10
m = 5

ret = solution(today, shelf_life, n, m)

print(ret)