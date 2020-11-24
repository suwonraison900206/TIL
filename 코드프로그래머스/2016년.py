def solution(a, b):
    answer = ''
    day_lst = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    mon_lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    count = 0

    for i in range(a-1):
        count = count + mon_lst[i]

    count = count + b

    c = count // 7
    d = count % 7
    print(c,d)

    print(count)
    answer = day_lst[d-1]
    print(answer)
    return answer

a = 5
b = 24

solution(a,b)