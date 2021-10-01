N = int(input())
N_lst = list(map(int,input().split()))
M = int(input())
M_lst = list(map(int,input().split()))

number_dict = {}

for i in N_lst:
    if i not in number_dict:
        number_dict[i] = 1
    else:
        number_dict[i] +=1

for i in M_lst:

    if i not in number_dict:
        print(0, end=' ')
    else:
        print(number_dict[i], end=' ')
