# import sys
# sys.stdin = open("1220.txt")

t = 1

for test_case in range(10):
    a = int(input())

    t =[([5] * (a)) for _ in range(a + 2)]
    # print(t)

    k = [list(map(int,input().split())) for _ in range(a)]

    for i in range(a):
        for j in range(a):
            t[i+1][j] = k[i][j]

    print(t)


    cnt = 1

    while cnt > 0:
        cnt = 0
        move = [([0] * (a)) for _ in range(a + 2)]
        for i in range(len(t)):
            for j in range(a):
                if t[i][j] == 1:
                    if t[i+1][j] == 5 and move[i][j] == 0:
                        t[i][j] = 0
                        move[i+1][j] = 1
                        cnt = cnt + 1
                    elif t[i+1][j] == 0 and move[i][j] == 0:
                        t[i][j] = 0
                        t[i+1][j] = 1
                        move[i+1][j] = 1
                        cnt = cnt + 1
                if t[i][j] == 2:
                    if t[i - 1][j] == 5 and move[i][j] == 0:
                        t[i][j] = 0
                        move[i-1][j] = 1
                        cnt = cnt + 1
                    elif t[i-1][j] == 0 and move[i][j] == 0:
                        t[i-1][j] = 2
                        t[i][j] = 0
                        move[i-1][j] = 1
                        cnt = cnt + 1
        print(t)


    #
    # print(t)


    count = 0
    for i in range(len(t)):
        for j in range(a):
            if t[i][j] == 1 or t[i][j] == 2:
                count = count + 1


    print(count)