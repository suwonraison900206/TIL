




t = int(input())


for test_case in range(t):

    a = int(input())

    test_in =[(list(map(int, input().split())))for _ in range(a)]


    final_result = []


    for i in range(1,a):

        for j in range(1,a):
            result = []
            sum1 = 0
            sum2 = 0
            sum3 = 0
            minv = 0

            for k in range(0, i):
                for d in range(0, j):
                    sum1 = sum1 + test_in[k][d]
            (result.append(sum1))
            for l in range(i, a):
                for b in range(0, j):

                    sum2 = sum2 + test_in[l][b]
            result.append(sum2)

            for m in range(0,a):
                for c in range(j,a):
                    sum3 = sum3 + test_in[m][c]
            result.append(sum3)

            minv = max(result) - min(result)
            final_result.append(minv)



    print(min(final_result))

