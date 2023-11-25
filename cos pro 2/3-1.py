def solution(k) :
    answer = []
    for i in range(1 , k + 1) :
        answer.append(i * i)
    return answer

n = 3
ret = solution(n)

print(ret)