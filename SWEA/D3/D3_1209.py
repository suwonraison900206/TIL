# import sys
# sys.stdin = open('1209.txt')


for test_case in range(1, 11):
    T = int(input())
    result = 0
    lst = [list(map(int,input().split())) for __ in range(100)]

    for i in lst:
        max_number = sum(i)

        if max_number > result:
            result = max_number

    for i in zip(*lst):
        max_number = sum(i)

        if max_number > result:
            result = max_number

    cnt = 0
    for i in range(len(lst)):
        cnt += lst[i][i]

    if result < cnt:
        result = cnt

    cnt = 0
    for i in range(len(lst)):

        cnt += lst[i][-i]

    if result < cnt:
        result = cnt

    print('#{} {}'.format(test_case,result))