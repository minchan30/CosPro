def solution(s) :
    answer = 0
    for c in s :
        if c >= 'A' and c <= 'Z' :
            answer += 1
    return answer

s = "AnSouluTE"
ret = solution(s)

print(ret)