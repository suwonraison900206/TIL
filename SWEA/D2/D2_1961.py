import sys
sys.stdin = open("1961.txt")

t = int(input())


for test_case in range(t):

    a = int(input())

    temp = [list(map(int,input().split())) for _ in range(a)]

    print('#{}'.format(test_case+1))
    for i in range(a):
        for k in range(1,a+1):  # 90도
            print(temp[-k][i], end='')
        print('', end=' ')
        for x in range(a):  # 180도
            print(temp[(a-1)-i][(a-1)-x], end='')
        print('', end=' ')
        for y in range(a): # 270도
            print(temp[y][(a-1)-i], end='')
        print()


    #
    #     for j in range(a-1, -1, -1):
    #         print(temp[j][i],end='')
    #
    #     print()
    # print('', end='')
    #
    # for i in range(a-1,-1,-1):
    #     for j in range(a-1,-1,-1):
    #         print(temp[i][j],end='')
    #     print()