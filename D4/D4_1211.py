

import sys
sys.stdin = open("1211.txt")


def my_min(list_a):
    result = list_a[0]
    result_idx = 0
    for a in range(1, len(list_a)):
        if list_a[a] != 0 and list_a[a] <= result:
            result = list_a[a]
            result_idx = a

    return result_idx


for test_case in range(10):
    a = int(input())
    test_in = []
    for i in range(100):
        test_in.append(list(map(int, input().split())))


    count = 0
    result2 = []
    for i in range(100):
        count = 0
        R = 0
        L = 0
        Y = 0
        if test_in[0][i] == 1:
            result = 0
            while Y < 99:
                if i - 1 >= 0 and i + 1 <= 99:  # 가운데 값 처리
                    if test_in[Y][i-1] == 0 and test_in[Y][i+1] == 0:
                        Y = Y + 1
                        count = count + 1
                    elif test_in[Y][i-1] == 1 and test_in[Y][i+1] == 1:
                        if R == 1:
                            i = i + 1
                            count = count + 1
                        elif L == 1:
                            i = i - 1
                            count = count + 1
                    elif test_in[Y][i-1] == 1 and test_in[Y][i+1] == 0:
                        if L == 1:
                            L = 1
                            Y = Y - 1
                            count = count + 1
                        elif R == 1:
                            R = 0
                            Y = Y + 1
                            count = count + 1
                        elif L == 0 and R == 0:
                            L = 1
                            i = i -1
                            count = count + 1
                    elif test_in[Y][i-1] == 0 and test_in[Y][i+1] == 1:
                        if L == 1:
                            L = 0
                            Y = Y +1
                            count = count + 1
                        elif R == 1:
                            R = 1
                            Y = Y + 1
                            count = count + 1
                        elif L == 0 and R == 0:
                            R = 1
                            i = i + 1
                            count = count + 1
                elif i - 1 < 0:  # 왼쪽 벽 붙을때
                    if test_in[Y][i+1] == 0 :
                        Y = Y + 1
                        count = count + 1
                    elif test_in[Y+1][i] == 1:
                        if L == 1:
                            L = 0
                            Y = Y + 1
                            count = count + 1
                        elif R == 0 :
                            R = 1
                            i = i + 1
                            count = count + 1
                elif i + 1 > 99:  # 오른 쪽 붙을때
                    if test_in[Y][i-1] == 0 :
                        Y = Y + 1
                        count = count + 1
                    elif test_in[Y][i-1] == 1:
                        if R == 1:
                            R = 0
                            Y = Y + 1
                            count = count + 1
                        else:
                            L = 1
                            i = i - 1
                            count = count + 1

            result2.append(count)
        else:
            result2.append(count)


    print('#{} {}'.format(test_case + 1, my_min(result2)))