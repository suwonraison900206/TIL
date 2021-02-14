def solution(play_time, adv_time, logs):

    if play_time == adv_time:
        return '00:00:00'

    play_h1 =int(play_time[0:2]) * 3600
    play_m1 = int(play_time[3:5]) * 60
    play_s1 = int(play_time[6:8])
    play_cnt = play_h1 + play_m1 + play_s1

    convert_lst = [0] * play_cnt
    result_lst = [0] * play_cnt

    stack = []
    for log in logs:

        h1 = int(log[0:2]) * 3600
        h2 = int(log[9:11]) * 3600
        m1 = int(log[3:5]) * 60
        m2 = int(log[12:14]) * 60
        s1 = int(log[6:8])
        s2 = int(log[15:17])
        stack.append([h1+ m1+ s1, h2 + m2 + s2])


    for i in range(len(stack)):
        for j in range(stack[i][0],stack[i][1]):
            convert_lst[j] += 1


    adv_h = int(adv_time[0:2]) * 3600
    adv_m = int(adv_time[3:5]) * 60
    adv_s = int(adv_time[6:8])
    adv_result = adv_h + adv_m + adv_s

    start = 0
    end = adv_result
    print(start, end)

    final =[start,end]
    final_cnt = sum(convert_lst[start:end])
    print(final_cnt)
    print(end, len(convert_lst))
    while end < len(convert_lst):
        





        break



    #
    # final_result = ''
    # final_h = final // 3600
    # final -= (final_h * 3600)
    # final_result = final_result + str(final_h).zfill(2) + ':'
    # final_m = final // 60
    # final -= (final_m * 60)
    # final_result = final_result + str(final_m).zfill(2) + ':'
    #
    # final_result = final_result + str(final).zfill(2)

    return

play_time = "99:59:59"
adv_time = 	"25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
solution(play_time, adv_time, logs)