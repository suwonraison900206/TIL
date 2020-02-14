t = int(input())

for test_case in range(t):
    b = list(map(int, input().split(' ')))

    result_index = 0

    result_list = []
    for i in range(b[0]):
        result = 0
        d = list(map(int, input().split(' ')))

        result = round((d[0] * 0.35) + (d[1] * 0.45) + (d[2] * 0.2),3)
        result_list.append(result)



    if result_list[b[1]-1] in result_list:
        a = result_list[b[1]-1]
        result_list.sort()
        result_index = result_list.index(a)



    if (((result_index + 1) / b[0]) * 100 ) <= 100 and (((result_index + 1) / b[0]) * 100 ) > 90:
        print('#{} A+'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 90 and (((result_index + 1) / b[0]) * 100 ) > 80:
        print('#{} AO'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 80 and (((result_index + 1) / b[0]) * 100 ) > 70:
        print('#{} A-'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 70 and (((result_index + 1) / b[0]) * 100 ) > 60:
        print('#{} B+'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 60 and (((result_index + 1) / b[0]) * 100 ) > 50:
        print('#{} BO'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 50 and (((result_index + 1) / b[0]) * 100 ) > 40:
        print('#{} B-'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 40 and (((result_index + 1) / b[0]) * 100 ) > 30:
        print('#{} C+'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 30 and (((result_index + 1) / b[0]) * 100 ) > 20:
        print('#{} CO'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 20 and (((result_index + 1) / b[0]) * 100 ) > 10:
        print('#{} C-'.format(test_case + 1))
    elif (((result_index + 1) / b[0]) * 100 ) <= 10 and (((result_index + 1) / b[0]) * 100 ) >= 0:
        print('#{} DO'.format(test_case + 1))








    #
    # if ((((result_index + 1) / b[0]) * 100 )+ 10) <= 100 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 90:
    #     print('#{} A+'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 90 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 80:
    #     print('#{} AO'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 80 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 70:
    #     print('#{} A-'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 70 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 60:
    #     print('#{} B+'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 60 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 50:
    #     print('#{} BO'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 50 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 40:
    #     print('#{} B-'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 40 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 30:
    #     print('#{} C+'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 30 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 20:
    #     print('#{} CO'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 20 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 10:
    #     print('#{} C-'.format(test_case + 1))
    # elif ((((result_index + 1) / b[0]) * 100 )+ 10) <= 10 and ((((result_index + 1) / b[0]) * 100 )+ 10) > 0:
    #     print('#{} DO'.format(test_case + 1))
