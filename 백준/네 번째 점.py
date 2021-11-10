lst = [list(map(int,input().split())) for _ in range(3)]

number_dic = {}
check= [[], []]
for x, y in lst:

    check[0].append(x)
    check[1].append(y)
for i in range(2):

    for j in range(len(check[i])):

        if check[i].count(check[i][j]) == 1:
            print(check[i][j], end=' ')