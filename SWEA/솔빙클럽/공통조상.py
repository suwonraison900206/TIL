import sys
sys.stdin = open("공통조상.txt")


T = int(input())

for test_case in range(T):

    V, E, Family_1, Family_2 = map(int,input().split())
    node_lst = list(map(int,input().split()))
    node_lst_2 = []
    visit_lst = [0] * (V + 1)
    visit_lst2 = [0] * (V + 1)

    stack = []
    for i in range(E//2):
        node_lst_2.append(node_lst[2*i:(2*i)+2])

    for i in range(len(node_lst_2)):
        if node_lst_2[i][1] == (Family_1 or Family_2) :
            print(node_lst_2)
            print(Family_1)
            print(Family_2)
            stack.append(node_lst_2[i])


    print(stack)

    while stack:
        k = stack.pop()
        print(k)
        break



