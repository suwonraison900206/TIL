import sys
from itertools import permutations, combinations
sys.stdin = open('5189.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    lst = [list(map(int,input().split())) for __ in range(N)]
    lst_2 = []
    for i in range(1, N):
        lst_2.append(i)
    k = list(permutations(lst_2, N - 1))
    count = []
    for i in range(len(k)):

        result_lst = []

        result_lst.append(0)
        for j in range(N-1):
            result_lst.append(k[i][j])
        result_lst.append(0)

        sum = 0
        for j in range(len(result_lst)-1):
            sum = sum + lst[result_lst[j]][result_lst[j+1]]
        count.append(sum)

    print('#{} {}'.format(test_case,min(count)))


