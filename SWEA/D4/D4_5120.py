T = int(input())

for test_case in range(T):
    N, M, K = map(int,input().split())
    count = 0
    count2 = 0
    q = 1
    lst = list(map(int,input().split()))

    while count != K:
        count2 = count2 + M  # + M번째 값 탐색
        if count2 < len(lst):
            lst.insert(count2, lst[count2-1] +lst[count2])
        elif count2 == len(lst):
            lst.insert(count2, lst[count2 - 1] + lst[0])
            count2 = -1
        elif count2 > len(lst):
            count2 = count2 - len(lst)
            lst.insert(count2, lst[count2 - 1] + lst[count2])

        count = count + 1  # K번 반복 횟수 카운트

    lst = lst[::-1]

    if len(lst) < 11:
        print('#{}'.format(test_case+1),end=' ')
        for i in range(len(lst)):
            print('{}'.format(lst[i]),end=' ')
        print()
    else:
        print('#{}'.format(test_case + 1), end=' ')
        for i in range(0, 10):
            print('{}'.format(lst[i]), end=' ')
        print()

