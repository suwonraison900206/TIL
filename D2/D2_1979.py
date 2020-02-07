T = int(input())


for test_case in range(T):
    list_k = []
    count_list = []
    sum = 0
    a = list(map(int, (input().split())))
    for i in range(a[0]):
        b = list(map(int, (input().split())))
        list_k.append(b)


    for i in range(a[0]):
        count = 1
        for j in range(a[0]-1):
            if list_k[i][j] == 1 and list_k[i][j+1] == 1:
                count = count + 1
                if j + 1 == a[0]-1:
                    count_list.append(count)
            else:
                count_list.append(count)
                count = 1
    for j in range(a[0]):
        count = 1
        for i in range(a[0] - 1):
            if list_k[i][j] == 1 and list_k[i+1][j] == 1:
                count = count + 1
                if i + 1 == a[0] - 1:
                    count_list.append(count)
            else:
                count_list.append(count)
                count = 1
    for i in range(len(count_list)):
        if count_list[i] == a[1]:
            sum = sum + 1

    print('#{} {}'.format(test_case + 1, sum))
