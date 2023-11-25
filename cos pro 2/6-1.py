def solution(umbrellas, rains) :

    answer = 0
    for rain in rains :
        if rain not in umbrellas :
            answer += 1
    return answer

umbrellas = ["2018/06/01", "2017/03/04", "2019/04/28"]
rains = ["2017/03/04", "2019/04/27"]
ret = solution(umbrellas, rains)

print(ret)