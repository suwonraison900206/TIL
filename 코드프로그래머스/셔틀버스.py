from datetime import datetime, timedelta


def solution(n, t, m, timetable):
    time_lst = []
    answer = 0
    for time in timetable:
        hour = int(time[0:2]) * 60
        minute = int(time[3:5])
        time_lst.append(hour + minute)
    time_lst.sort(reverse=True)
    bus_start = 540
    bus_lst = []

    for i in range(n):
        bus_lst.append(540 + (i * t))
    bus_lst.sort(reverse=True)

    for j in range(len(bus_lst)-1, -1, -1):

        number = m
        if not time_lst:
            break
        for i in range(len(time_lst)-1, -1, -1):

            if not time_lst:
                break
            if time_lst[i] <= bus_lst[j]:
                if number != 0:
                    k = time_lst.pop()
                    number -= 1
                else:
                    break

    if not time_lst:
        answer = k - 1
    else:
        answer = bus_lst[0]

    if answer <= 540:
        answer = 540

    hour, minute = answer // 60, answer % 60

    # 답에 맞게 문자열 처리
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)

    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    answer = hour + ':' + minute
    print(answer)
    return answer



n = 10
t = 60
m = 45
timetable = 	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
solution(n,t,m,timetable)