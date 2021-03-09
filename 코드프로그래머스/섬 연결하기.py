from collections import deque

def solution(n, costs):
    answer = 0

    island = [[float('inf')] * n for __ in range(n)]


    nodes = [[] * n for __ in range(n)]
    costs.sort(key=lambda x:x[0])
    for u,v,d in costs:
        nodes[u].append([v,d])
        nodes[v].append([u,d])
    print(nodes)


    for number in range(n):
        island[number][number] = 0
        queue = deque([number])

        while queue:
            q = queue.popleft()
            for next, d in nodes[q]:
                if island[number][q] + d < island[number][next]:
                    island[number][next] = island[number][q] + d
                    queue.append(next)
    print(island)
    count = 0

    for number in range(n):
        island[number][number] = float('inf')

    for i in range(1, len(island)):

        count = count + min(island[i])

    print(count)

    return count

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(n,costs)