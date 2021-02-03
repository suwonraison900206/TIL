from collections import deque

def solution(n, edge):
    answer = 0
    dist = [float('inf')] * (n+1)
    dist[0] = 0
    dist[1] = 0
    nodes = [[] * (n+1) for __ in range(n+1)]
    for u,v in edge:

        nodes[u].append([v,1])
        nodes[v].append([u,1])
    queue = deque([1])
    while queue:
        q = queue.popleft()

        for destination, d in nodes[q]:

            if dist[q] + d < dist[destination]:
                dist[destination] = dist[q] + d
                queue.append(destination)

    max_value = max(dist)

    for i in dist:
        if i == max_value:
            answer += 1

    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n,vertex)