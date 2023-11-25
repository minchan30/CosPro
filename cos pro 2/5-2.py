def solution(s) :
    answer = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for c in s :
        if c in vowel :
            answer += 1
    return answer

s = "Megastudy"
ret = solution(s)

print(ret)