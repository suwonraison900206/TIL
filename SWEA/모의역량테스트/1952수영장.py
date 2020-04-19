import sys
sys.stdin = open("swim2.txt")

t = int(input())

for test_case in range(t):
    d_f, m_f, t3_f, y_f = list(map(int,input().split()))
    month = list(map(int,input().split()))
    m_list = []
    cnt = 0
    for i in range(len(month)):
        m_list2 = []
        m_list2.append(month[i])
        m_list.append(m_list2)
    m_list.append([0])
    day_result = []

    for i in range(len(m_list)):
        if m_list[i][0] * d_f > m_f:
            day_result.append(m_f)
        else:
            day_result.append(m_list[i][0] * d_f)



    final_result= []

    for i in range(len(day_result)-1):

        if i == 2:
            if cnt + day_result[i] > t3_f:
                cnt = t3_f
                final_result.append(cnt)
            else:
                cnt = cnt + day_result[i]
                final_result.append(cnt)
        elif i >= 3:
            if day_result[i] == 0:
                final_result.append(cnt)

            else:
                if cnt + day_result[i] < final_result[i-3] + t3_f:
                    cnt = cnt + day_result[i]
                    final_result.append(cnt)
                else:
                    cnt = final_result[i-3] + t3_f
                    final_result.append(cnt)
        else:
            cnt = cnt + day_result[i]
            final_result.append(cnt)
    if cnt > y_f:
        print('#{} {}'.format(test_case+1, y_f))
    else:
        print('#{} {}'.format(test_case + 1, cnt))





