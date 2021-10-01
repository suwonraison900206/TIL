while True:
    lst = list(map(int,input().split()))
    lst.sort()
    if sum(lst) == 0:

        break

    else:
        if lst[0] **2 + lst[1] **2 == lst[2] **2:
            print('right')

        else:
            print('wrong')


