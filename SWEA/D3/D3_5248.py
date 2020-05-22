# -*- coding: cp949 -*-
import sys
sys.stdin = open('5248.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    visit = [0] * (N + 1)
    stack = []
    stack.append(lst[0])
    stack.append(lst[1])
    visit[lst[0]] = 1
    visit[lst[1]] = 1
    lst.pop(0)
    lst.pop(0)
    count = 0

    while lst:
        if len(stack) == 0:
            stack.append(lst[0])
            stack.append(lst[1])
            visit[lst[0]] = 1
            visit[lst[1]] = 1
            lst.pop(0)
            lst.pop(0)

        action = 0

        for i in range(len(lst)):
            if lst[i] in stack:
                if i % 2 == 0:
                    stack.append(lst[i+1])
                    visit[lst[i+1]] = 1
                    lst.pop(i)
                    lst.pop(i)
                    action = 1
                    break
                elif i % 2 == 1:
                    stack.append(lst[i-1])
                    visit[lst[i - 1]] = 1
                    lst.pop(i)
                    lst.pop(i-1)
                    action = 1
                    break

        if action == 0 and len(lst) != 0:
            count = count + 1
            stack = []

    if len(stack) != 0:
        count = count + 1

    for i in range(len(visit)):
        if visit[i] == 0:
            count = count + 1

    print('#{} {}'.format(test_case, count -1))







