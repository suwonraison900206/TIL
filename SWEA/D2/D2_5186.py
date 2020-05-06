T = int(input())
for tc in range(1, 1+T):
    N = float(input())
    result, idx = '', -1
    while N != 0:
        if len(result) > 13:
            result = 'overflow'
            break
        if N - 2 ** idx >= 0:
            N -= 2 ** idx
            result += '1'
        else:
            result += '0'
        idx -= 1
    print('#{0} {1}'.format(tc, result))