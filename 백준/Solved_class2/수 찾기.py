N = int(input())
N_lst = list(map(int,input().split()))
M = int(input())
M_lst = list(map(int,input().split()))
number_dict = {}

for i in N_lst:
    number_dict[i] = 1

for i in M_lst:

    if i not in number_dict:
        print(0)
    else:
        print(1)