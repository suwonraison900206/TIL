
t = int(input())

for test_case in range(t):

    a = str(input())
    b = []
    cnt = 0

    for i in range(1,16):
        if a[0:i] == a[i:i+i]:
           cnt = cnt + i
           break
    print('#{} {}'.format(test_case+1, cnt))