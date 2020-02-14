
t = int(input())

for test_case in range(t):
    l = list(map(int, input().split()))
    k = list(map(str, input().split()))
    count = 1
    result = []


    for i in range(l[0]-1):

        if k[0][i] == '1' and k[0][i+1] == '1':
            count = count + 1
        else:
            result.append(count)
            count = 1
    result.append((count))
    print('#{} {}'.format(test_case+1, max(result)))