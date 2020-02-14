
t = int(input())
for testcase in range(t):
    print('#{}'.format(testcase + 1),end=' ')
    temp_len = int(input())
    temp = list(map(int, input().split()))
    for i in range(len(temp)-1, 0, -1) :
        for j in range(0, i):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]

    short_temp = temp[:5]
    reverse_short_temp = temp[:4:-1]


    for i in range(5):
        print('{} {}'.format(reverse_short_temp[i], short_temp[i]),end= ' ')

    print()
