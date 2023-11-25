def solution(n) :
    answer = 1
    for i in range(1 , n + 1) :
        answer *= i
    answer = answer + n
    return answer

n = 5
ret = solution(n)

print(ret)