N = int(input())

lst = [list(input().split()) for __ in range(N)]

lst.sort(key=lambda x:(len(x[0]) , x[0]))
check_dict = {}

for i in lst:

    for j in i:
        if j not in check_dict:

            check_dict[j] = 1
            print(j)
        else:
            pass