t = int(input())

for test_case in range(t):
    a = str(input())

    b = a[::-1]

    if a == b:
        print('#{} 1'.format(test_case + 1))
    else:
        print('#{} 0'.format(test_case + 1))
    