t = int(input())

for test_case in range(t):
    k = list(str(input()))

    result_list = []

    quit =0
    cnt = 0
    cnt2 = 0
    for i in range(len(k)):
        if k[i] == ')':
            if cnt == 0:
                quit = quit + 1
                print('#{} 0'.format(test_case + 1))
                break
            elif k[i-1] == '{':
                quit = quit + 1
                print('#{} 0'.format(test_case + 1))
                break

            else:
                cnt = cnt -1
        elif k[i] == '}':
            if cnt2 == 0:
                quit = quit +1
                print('#{} 0'.format(test_case + 1))
                break
            elif k[i-1] == '(':

                quit = quit +1
                print('#{} 0'.format(test_case + 1))
                break
            else:
                cnt2 = cnt2 -1
        elif k[i] == '(':
            cnt = cnt + 1
        elif k[i] == '{':
            cnt2 = cnt2 +1

    if quit == 0:
        if cnt != 0 or cnt2 != 0 :
            print('#{} 0'.format(test_case+1))
        else:
            print('#{} 1'.format(test_case+1))
