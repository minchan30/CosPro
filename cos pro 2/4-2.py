def solution(number, str) :
    
    answer = 0
    for i in range(5) :
        if number[i] % 2 == 0 :
            if str[i] == '짝' :
                answer += 1
        else :
            if str[i] == '홀' :
                answer += 1

    return answer

number = [1, 4, 6, 2, 8]
str = ['홀', '짝', '홀', '짝', '홀']
ret = solution(number, str)

print(ret)