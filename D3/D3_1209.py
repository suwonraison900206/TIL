
temp = []
final_result = []
for i in range(10):
    result = []
    c = int(input())
    test_in = []
    for i in range(100):
       + temp = list(map(int, input().split()))
        test_in.append(temp)
    reverse_test_in = test_in[::-1]
    cnt = 0

    for i in range(len(test_in)):
        sum = 0
        for j in range(len(test_in[0])):
            sum = sum + test_in[i][j]
        result.append(sum)

    for j in range(len(test_in[0])):
        sum = 0
        for i in range(len(test_in)):
            sum = sum + test_in[i][j]
        result.append(sum)

    sum = 0
    for i in range(len(test_in)):

        sum = sum + test_in[i][cnt]
        cnt = cnt + 1
    result.append((sum))

    sum = 0
    cnt = 0
    for i in range(len(reverse_test_in)):
        sum = sum + reverse_test_in[i][cnt]
        cnt = cnt + 1
    result.append((sum))

    final_result.append(max(result))

    # result_max = max(result)
    # final_result.append(result_max)
    #


for i in range(10):
    print('#{0} {1}'.format(i+1 , final_result[i]))
