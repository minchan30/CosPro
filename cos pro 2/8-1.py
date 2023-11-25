def solution(k) :
    answer = [False] * 10
    for person in range(1, k + 1) :
        for multiple in range(person, 11, person) :
            answer[multiple - 1] = not answer[multiple - 1]
    return answer
    
k = 2
ret = solution(k)

print(ret)