def func_a(val1, val2) :
    return val1 - val2

def  func_b(arr) :
    answer = arr[0]
    for elem in arr :
        if answer < elem :
            answer = elem
    return answer

def func_c(arr) :
    answer = arr[0]
    for elem in arr :
        if answer > elem:
            answer = elem
    return answer
def solution(scores) :
    max_val = func_b(scores)
    min_val = func_c(scores)
    answer = func_a(max_val, min_val)
    return answer

scores = [70, 30, 20, 85, 50]
ret = solution(scores)

print(ret)