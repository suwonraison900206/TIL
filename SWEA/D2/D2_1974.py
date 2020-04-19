import sys
sys.stdin = open("1974.txt")

t = int(input())

number =[1, 2, 3, 4, 5, 6, 7, 8, 9]

for test_case in range(t):
    temp = [list(map(int,input().split())) for _ in range(9)]

    result1 = []
    result2 = []
    result3 = []

    for i in range(3):
        for j in range(3):
            result = []
            for x in range(3*i,(3*i)+3):
                for y in range(3*j,(3*j)+3):
                    result.append(temp[x][y])
            list.sort(result)
            result1.append(result)
    for i in range(9):
        result = []
        for j in range(9):
            result.append(temp[i][j])
        list.sort(result)
        result2.append(result)
    for i in range(9):
        result = []
        for j in range(9):
            result.append(temp[j][i])
        list.sort(result)
        result3.append(result)
    cnt = 0
    for i in range(9):
        if result1[i] != number or result2[i] != number or result3[i] != number:
            print('#{} 0'.format(test_case+1))
            cnt = cnt +1
            break

    if cnt == 0:
        print('#{} 1'.format(test_case+1))









    #
    #
    # for i in range(len(result1)):

