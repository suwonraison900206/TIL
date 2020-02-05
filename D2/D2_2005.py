
a = int(input())
k = 0
for test_case in range(a):
    b = int(input())



    pascal = [[1 for _ in range(i)] for i in range(1, b+1)]


    for i in range(2,b ):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]




    print('#{}'.format(test_case +1))
    for i in range(b):
        k = ' '.join(map(str, pascal[i]))
        print(k)
    #
    #
    # print(pascal[4])


    #
    # for i in range(b):
    #     print(pascal)
    #
    #     for j in range(1, i):
    #         pascal[i][j] = pascal[i][j]
    #


    # print('#{} {}'.format(test_case +1, pascal))