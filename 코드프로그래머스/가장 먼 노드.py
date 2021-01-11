def solution(n, edge):
    answer = 0
    edge.sort()
    print(edge)
    n_lst = [0] * n

    for i in range(len(edge)):

        if n_lst[edge[i][0] -1] == 0:
            if n_lst[edge[i][1] -1] == 0:
                n_lst[edge[i][1]-1] = 1
            else:
                n_lst[edge[i][0] -1] = n_lst[edge[i][1]-1] + 1
        else:
            if n_lst[edge[i][0]-1] != 0 and n_lst[edge[i][1] -1] != 0:
                pass
            elif n_lst[edge[i][0]-1] != 0 and n_lst[edge[i][1] -1] == 0:
                n_lst[edge[i][1]-1] = n_lst[edge[i][0] -1] + 1
            elif n_lst[edge[i][0] - 1] == 0 and n_lst[edge[i][1] - 1] != 0:
                n_lst[edge[i][0]-1] = n_lst[edge[i][1]-1] + 1
        print(edge[i])
        print(n_lst)
    print(n_lst.count(max(n_lst)))

    return n_lst.count(max(n_lst))



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n,vertex)