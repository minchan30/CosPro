def solution(buy_list, market) :

    answer = 0
    for i in buy_list :
        if i in market :
            answer += 1
    return answer

buy_list = ['수요일 : 당근', '목요일 : 시리얼', '금요일 : 햇반']
market = ['월요일 : 소고기',
'화요일 : 당근',
'수요일 : 시리얼',
'목요일 : 연어',
'금요일 : 햇반',
'토요일 : 샐러드',
'일요일 : 마라탕']

ret = solution(buy_list, market)

print(ret)