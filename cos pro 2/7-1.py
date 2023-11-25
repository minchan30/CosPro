def func_a(arr) :
    answer = [-1]
    for i in range(1, len(arr)) :
        answer.append(arr[i] - arr[i - 1])
    return answer

def func_b(arr) :
    return arr[-1]

def func_c(arr) :
    arr.sort()

def solution(sales) :
    diff = func_a(sales)
    func_c(diff)
    return func_b(diff)

sales = [50, 25, 45, 75, 30]
ret = solution(sales)

print(ret)