import sys
sys.stdin = open("5122.txt")

T = int(input())

for test_case in range(T):
    N, M, L = map(int,input().split())

    lst = list(map(int,input().split()))
    for k in range(M):
        stack = list(input().split())
        if stack[0] == 'I':
            lst.insert(int((stack[1])),int((stack[2])))
        elif stack[0] == 'D':
            lst.pop(int(stack[1]))
        elif stack[0] == 'C':
            lst[int(stack[1])] = int(stack[2])
    if len(lst) >= L:
        print('#{} {}'.format(test_case+1,lst[L]))
    else:
        print('#{} -1'.format(test_case+1))