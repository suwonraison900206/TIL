import sys
sys.stdin = open("5105.txt")

T = int(input())

for test_case in range(T):

    N = int(input())

    lst = []
    for i in range(N):
        lst.append(list(map(int, input())))

    visit_lst = [[0] * N for __ in range(N)]


    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = []
    stack2 = []

    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] == 2:
                stack.append((i, j))
    result = 0
    count = 0
    while stack:
        K = stack.pop(0)
        for i in range(4):
            di = K[0] + dx[i]
            dj = K[1] + dy[i]
            if 0 <= di < N and 0 <= dj < N:
                if visit_lst[di][dj] == 0 and lst[di][dj] == 0:
                    stack2.append((di,dj))
                    visit_lst[di][dj] = 1
                elif lst[di][dj] == 3 and visit_lst[di][dj] == 0:
                    result = result + 1
                    visit_lst[di][dj] = 1
                    print('#{} {}'.format(test_case+1,count))
                    break

        if len(stack) == 0 and result == 0:
            stack = stack2
            stack2 = []
            count = count + 1
    if result == 0:
        print('#{} 0'.format(test_case+1))







