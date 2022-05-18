from collections import deque

def solution(n, s, a, b, fares):
    dist = [[float('inf')] * (n+1) for __ in range (n+1)]
    nodes = [[] * (n+1) for __ in range(n+1)]
    for u, v, d in fares:
        nodes[u].append([v, d])
        nodes[v].append([u, d])

    for number in range(1, n+1):
        dist[number][number] = 0
        queue = deque([number])
        while queue:
            q = queue.popleft()
            for next, d in nodes[q]:
                if dist[number][q] + d < dist[number][next]:
                    dist[number][next] = dist[number][q] + d
                    queue.append(next)

    cnt = float('inf')
    for i in range(1,len(dist[s])):
        if dist[s][i] + dist[i][a] + dist[i][b] < cnt:
            cnt = dist[s][i] + dist[i][a] + dist[i][b]
    print(cnt, dist)
    return cnt

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n, s, a, b, fares)
