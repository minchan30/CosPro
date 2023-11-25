def solution(numbers, a, b) :
    answer = []
    for number in numbers :
        if a < number and number < b :
            answer.append(number)
    return answer

numbers = [3, 4, 1, 2, 6, 7, 2, 5]
a = 2
b = 4
ret = solution(numbers, a, b)

print(ret)