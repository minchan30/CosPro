def hhmm_to_int(hhmm) :
    hh, mm = hhmm.split(':')
    return int(hh) * 60 + int(mm)

def solution(start, attendances, n, m) :
    answer = []
    start = hhmm_to_int(start)
    for attendance in attendances :
        attendance = hhmm_to_int(attendance)
        if attendance <= start + n :
            answer.append(0)
        elif attendance <= start + m :
            answer.append(1)
        else :
            answer.append(2)
    return answer

start = "09:00"
attendances = ["09:10", "09:30", "09:31"]
n = 10
m = 30

ret = solution(start, attendances, n, m)

print(ret)