from collections import deque


def solution(N, road, K):
    answer = 0
    lst = [float('inf')] * (N + 1)
    lst[1] = 0
    node = {}
    cnt = 0

    for u, v, dist in road:
        print(u,v,dist, node)
        if u not in node[v]:
            node[u] = {v: [dist]}
        else:
            node[u][v].append(dist)

        if v not in node:
            node[v] = {u: [dist]}
    print(node)
    print(node[1][2])
    #     while queue:
    #         target = queue.popleft()
    #         for key, value in node[target].items():
    #             if lst[key] > lst[target] + value:
    #                 lst[key] = lst[target] + value
    #                 queue.append(key)

    #     print(lst)

    return cnt


N = 6
road = 	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
k = 4
solution(N, road, k)