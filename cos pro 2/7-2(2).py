def func_a(val, val2) :
    return val - val2

def func_b(arr) :
    answer = arr[0]
    for elem in arr :
        if answer < elem :
            answer = elem
    return answer

def func_c(arr) :
    answer = arr[0]
    for elem in arr :
        if answer > elem :
            answer = elem
    return answer

def func_d(arr) :
    total = 0
    for i in arr :
        total += i
    return total // len(arr)

def  solution(scores) :
    max_val = func_b(scores)
    min_val = func_c(scores)
    scores.remove(max_val)
    scores.remove(min_val)
    answer = func_d(scores)
    return answer

scores = [70, 20, 40, 85, 50]
ret = solution(scores)

print(ret)