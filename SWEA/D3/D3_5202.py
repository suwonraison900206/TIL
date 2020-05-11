import sys
import copy
sys.stdin = open('5202.txt')

def backtracking(number, index, count):
    global time_sort
    global final_result
    if index >= (len(time_sort) -1):
        final_result.append(count)
        return

    for i in range(index+1 , len(time_sort)):
        if number <= time_sort[i][0]:
            backtracking(time_sort[i][1], i, count+1)
    final_result.append(count)
    return



T = int(input())

for test_case in range(T):
    N = int(input())
    time_lst = [list(map(int,input().split())) for __ in range(N)]
    time_lst2 = []
    time_sort = []
    final_result = []
    while time_lst:
        for i in range(len(time_lst)):
            time_lst2.append(time_lst[i][0])

        time_lst2.sort()

        for i in range(len(time_lst2)):
            for j in range(len(time_lst)):
                if time_lst2[i] == time_lst[j][0]:
                    time_sort.append(time_lst[j])
                    time_lst.pop(time_lst.index(time_lst[j]))
                    break
        break
    for i in range(len(time_sort)):
        backtracking(time_sort[i][1], i, 1)

    print('#{} {}'.format(test_case+1, max(final_result)))









