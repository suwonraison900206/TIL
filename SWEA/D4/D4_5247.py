# -*- coding: utf-8 -*-
import sys , copy
from _collections import deque
sys.stdin = open('5247.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    visit_lst = [0] * 1000001
    stack = deque()
    stack_append = stack.append
    stack_append(N)
    stack2 = deque()
    count = 0

    while stack:
        q = stack.popleft()

        if q == M:
            print('#{} {}'.format(test_case, count))
            break
        if q + 1 <= 1000000 and visit_lst[q + 1] == 0:
            visit_lst[q + 1] = 1
            stack2.append(q+1)
        if q - 1 > -1 and visit_lst[q - 1] == 0:
            visit_lst[q - 1] = 1
            stack2.append(q - 1)
        if (q * 2) <= 1000000 and visit_lst[(q * 2)] == 0:
            visit_lst[q * 2] = 1
            stack2.append(q * 2)
        if q - 10 > -1 and visit_lst[q - 10] == 0:
            visit_lst[q - 10] = 1
            stack2.append(q - 10)

        if len(stack) == 0 and len(stack2) != 0:
            stack = copy.deepcopy(stack2)
            stack2 = deque()
            count = count + 1





