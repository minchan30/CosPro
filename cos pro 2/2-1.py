def solution(numbers, a, b) :
    answer = 0
    for number in numbers :
        if number < a or number > b :
            answer += 1
    return answer

numbers = [3, 4, 1, 2, 5]
a = 2
b = 4
ret = solution(numbers, a, b)

print(ret)