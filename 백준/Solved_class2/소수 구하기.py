M, N = map(int,input().split())


for i in range(M, N+1):
    if i == 1:
        continue
    if i == 2:
        print(2)
        continue
    flag = 0
    if int(i ** 0.5) +1 < 2:
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)

    else:

        for j in range(2, int(i ** 0.5) +1):

            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)
