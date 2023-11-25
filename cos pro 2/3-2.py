def solution(k) :
    answer = 0
    for i in range(1, k + 1) :
        answer += i * i
    return answer

n = 3
ret = solution(n)

print(ret)