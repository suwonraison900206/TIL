import sys
sys.stdin = open("4871.txt")


t = int(input())

for test_case in range(t):
    temp = list(map(int,input().split()))
    list_k = [list(map(int,input().split())) for _ in range(temp[1])]
    result_list = list(map(int,input().split()))
    node_list = [[0] * (temp[0] + 1) for _ in range(temp[0] + 1)]

    stack = []
    visit_list =[[0] * (temp[0]+1) for _ in range(temp[0]+1)]
    stack_result = []
    cnt = 0

    for i in range(temp[1]):
        node_list[list_k[i][0]][list_k[i][1]] = 1

    stack.append(result_list[0])

    while stack:
        v = stack.pop()
        if v == result_list[1]:
            cnt = cnt +1
            print('#{} {}'.format(test_case+1,cnt))
            break
        for j in range(len(node_list)):
            if node_list[v][j] == 1 and visit_list[v][j] ==0:
                stack.append(j)

    if cnt == 0:
        print('#{} {}'.format(test_case+1,cnt))
















