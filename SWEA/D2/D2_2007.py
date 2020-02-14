
t = int(input())

for test_case in range(t):

    a = str(input())
    b = []
    cnt = 0
    for i in range(1,11):
        if a[0:i] == a[i:i+i]:
            if a[i:i+i] == a[-i:30]:
                if cnt == 0:
                    cnt = cnt + i
                    break
    for j in range(10,16):
        if a[0:j] == a[j: j+j]:
            if cnt == 0:
                cnt = cnt + j
    print('#{} {}'.format(test_case+1, cnt))