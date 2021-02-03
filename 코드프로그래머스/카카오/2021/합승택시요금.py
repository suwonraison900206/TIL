from collections import deque

def solution(n, s, a, b, fares):
    answer = 0
    print(n,s,a,b,fares)
    dist = [[float('inf')] * (n+1) for __ in range (n+1)]
    print(dist)

    nodes = [[] * (n+1) for __ in range(n+1)]
    print(nodes)
    for u ,v ,d in fares:
        nodes[u].append([v, d])
        nodes[v].append([u, d])
    print(nodes)
    print(dist)
    for number in range(1, n+1):
        dist[number][number] = 0
        queue = deque([number])
        while queue:
            q = queue.popleft()
            for next, d in nodes[q]:
                if dist[number][q] + d < dist[number][next]:
                    dist[number][next] = dist[number][q] + d
                    queue.append(next)

    stack = []
    for i in range(1,len(dist[s])):
        count = dist[s][i]

        for j in range(1, len(dist[i])):
            count = count + dist[i][a] + dist[i][b]
            stack.append(count)
    print(stack)
    print(min(stack))
    answer = min(stack)

    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n, s, a, b, fares)
