import sys
sys.stdin = open("1238.txt")

T = 10

for test_case in range(T):
    people = 100
    visited_lst = [0] * (people+1)
    stack = []
    stack2 = []
    result_list = []
    K, N = map(int, input().split())
    lst = list(map(int, input().split()))
    stack.append(N)
    while stack:
        K = stack.pop()
        for j in range(0,len(lst), 2):
            if lst[j] == K and visited_lst[lst[j+1]] == 0:
                visited_lst[K] = 1
                visited_lst[lst[j+1]] = 1
                stack2.append(lst[j+1])
        if len(stack) == 0:
            if len(stack2) != 0:
                stack = stack2
                result_list = stack[:]
                stack2 = []
            else:
                print('#{} {}'.format(test_case+1, max(result_list)))




