t = 1


for test_case in range(t):
    a = list(input().split())
    b = list(input().split())

    print(a)
    print(b)

    c = []
    for i in range(len(b[0])-len(a[0])+1):
        c = c + (b[i:i+len(a[0])])

    print(c)



    if a in b:
        print('#{} 1'.format(test_case+1))
    else:
        print('#{} 0'.format(test_case + 1))