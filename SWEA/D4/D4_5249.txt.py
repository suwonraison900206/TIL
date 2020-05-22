import sys
from _collections import deque
sys.stdin = open('5249.txt', 'r')

T = int(input())

for test_case in range(1, T+1):

    V , M = map(int,input().split())

    node_lst = [list(map(int,input().split())) for __ in range(M)]
    node_lst.sort(key=lambda x: x[2])
    node_lst =deque(node_lst)
    visit_lst = [0] * (M)
    stack = deque()
    weight = 0

    while node_lst:
        k = node_lst.popleft()
        if 0 not in visit_lst:
            break
        if visit_lst[k[0]] == 1 and visit_lst[k[1]] == 1:
            pass
        elif visit_lst[k[0]] == 0 and visit_lst[k[1]] == 0:
            visit_lst[k[0]] = 1
            visit_lst[k[1]] = 1
            stack.append(k[0])
            stack.append(k[1])
            weight = weight + k[2]
        elif visit_lst[k[0]] == 0 and visit_lst[k[1]] == 1:
            visit_lst[k[0]] = 1
            stack.append(k[0])
            weight = weight + k[2]
        elif visit_lst[k[0]] == 1 and visit_lst[k[1]] == 0:
            visit_lst[k[1]] = 1
            stack.append(k[1])
            weight = weight + k[2]


    print('#{} {}'.format(test_case,weight))