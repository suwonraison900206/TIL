t = int(input())


for test_case in range(t):
    a = list(input())
    b = list(input())
    c = []
    cnt = 0
    for i in range(len(b)-len(a)+1):
        c = b[i:i+len(a)]
        if c == a:
            print('#{} 1'.format(test_case+1))
            cnt = cnt +1
            break

    if cnt == 0:
        print('#{} 0'.format(test_case + 1))