import sys
sys.stdin = open("상원.txt")

T = int(input())

for test_case in range(T):
    N, M = map(int,input().split())
    M_lst = [list(map(int,input().split())) for __ in range(M)]
    visit = [0] * (N+1)
    stack = []
    stack2 = []
    count = 0
    result = 0
    visit[1] = 1
    for i in range(len(M_lst)):
        if M_lst[i][0] == 1:
            stack.append(M_lst[i][1])
            visit[M_lst[i][1]] = 1
            result += 1

    while stack:
        if count == 1:
            break
        k = stack.pop(0)
        for j in range(len(M_lst)):
            if (M_lst[j][0] == k and visit[M_lst[j][1]] == 0) or (M_lst[j][1] == k and visit[M_lst[j][0]] == 0) :
                stack2.append(M_lst[j][1])
                stack2.append(M_lst[j][0])
                visit[M_lst[j][1]] = 1
                visit[M_lst[j][0]] = 1
                result += 1

        if len(stack) == 0:
            stack = stack2[:]
            stack2 = []
            count = count + 1
    if result == 0:
        print('#{} {}'.format(test_case + 1, result))
    else:
        print('#{} {}'.format(test_case +1, result))




