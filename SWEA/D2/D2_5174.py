import sys
sys.stdin = open("5174.txt")

T = int(input())

for test_case in range(T):

    E, N = map(int,input().split())
    visit_lst = [[0] * (E+2) for __ in range(E+2)]
    tree_lst = [[0] * (E+2) for __ in range(E+2)]
    node_lst = list(map(int,input().split()))
    stack = []
    count = 0
    for i in range(0,len(node_lst),2):
        tree_lst[node_lst[i]][node_lst[i+1]] = 1


    stack.append(node_lst[0])

    while stack:
        k = stack.pop()

        for i in range(0, len(node_lst),2):
            if count == 0:
                if node_lst[i] == k:
                    if node_lst[i+1] == N:
                        stack = []
                        stack.append(node_lst[i+1])
                        count += 1
                        break
                    else:
                        stack.append(node_lst[i+1])
            elif count != 0:
                if node_lst[i] == k:
                    stack.append(node_lst[i+1])
                    count += 1
    print('#{} {}'.format(test_case+1, count))















