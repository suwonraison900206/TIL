t = int(input())

for test_case in range(t):
    a = int(input())

    c = 0
    for i in range(1, a+1):
        c = c +  (i * ((-1) **(i+1)))
    print('#{} {}'.format(test_case + 1, c))