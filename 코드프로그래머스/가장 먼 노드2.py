import collections


def solution(n, vertex):
    dists = {i: 0 for i in range(1, n + 1)}  # (1)
    edge = collections.defaultdict(list)
    print(dists)
    print(edge)
    for v, u in vertex:  # (2)
        edge[v].append(u)
        edge[u].append(v)

    print(edge)


    q = collections.deque(edge[1])  # (3)
    dist = 1
    print(q)
    while q:
        print(q, 'q')
        for i in range(len(q)):
            v = q.popleft()

            if dists[v] == 0:
                dists[v] = dist

                for w in edge[v]:
                    q.append(w)
        dist += 1
    print(dist , 'dist')
    del dists[1]  # (4)

    max_value = max(dists.values())

    answer = 0
    for v in dists.values():  # (5)
        if v == max_value:
            answer += 1

    return answer



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n,vertex)