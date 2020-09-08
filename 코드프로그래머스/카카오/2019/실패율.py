def solution(N, stages):
    k = [0] * len(stages)
    answer = []

    clear_stage = [0] * (N+1)

    result_lst = []
    cnt = len(stages)

    for i in range(len(stages)):
        clear_stage[stages[i]-1] += 1

    fail_percentage = []
    for i in range(len(clear_stage)):
        if cnt !=0:
            fail_percentage.append((clear_stage[i]/cnt , i+1))
            cnt = cnt - clear_stage[i]
        elif cnt == 0:
            fail_percentage.append((0,i+1))

    fail_percentage.pop(-1)
    fail_percentage.sort(key=lambda x:x[0] , reverse=True)

    for i in range(len(fail_percentage)):
        answer.append(fail_percentage[i][1])

    return answer


N = 4
stages = [4,4,4,4,4]

solution(N, stages)