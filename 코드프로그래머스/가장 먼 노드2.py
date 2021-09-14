import heapq

def solution(n, edge):
    answer = 0
    dist = [float('inf')] * (n+1)
    dist[0] = 0
    dist[1] = 0
    nodes = {}

    for i in edge:
        if i[0] not in nodes:
            nodes[i[0]] = [i[1]]
        else:
            nodes[i[0]].append(i[1])

        if i[1] not in nodes:
            nodes[i[1]] = [i[0]]
        else:
            nodes[i[1]].append(i[0])

    heap = []
    heapq.heappush(heap, [1,0])
    while heap:

        node, weight = heapq.heappop(heap)
        for j in nodes[node]:

            if weight + 1 < dist[j]:
                heap.append([j, weight+1])
                dist[j] = weight+1


    return dist.count(max(dist))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n,vertex)