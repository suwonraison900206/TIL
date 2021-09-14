from collections import deque

def solution(n, s, a, b, fares):
    dist = [[float('inf')] * (n+1) for __ in range (n+1)]
    nodes = [[] * (n+1) for __ in range(n+1)]
    for u ,v ,d in fares:
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

    cnt = 10000000
    for i in range(len(dist)):

        print(dist[i])
    for i in range(1,len(dist[s])):
        print(dist[s][i] + dist[i][a] + dist[i][b] )
        if dist[s][i] + dist[i][a] + dist[i][b] < cnt:
            cnt = dist[s][i] + dist[i][a] + dist[i][b]

    return cnt




#
#
#
# from collections import defaultdict
# import heapq
#
# def solution(n, s, a, b, fares):
#     dic = defaultdict(list)
#     for st, ed, co in fares:
#         dic[st].append((co, ed))
#         dic[ed].append((co, st))
#     ans = []
#     for i in range(1, n+1):
#         Q = [(0, i)]
#         visited = [True] * (n+1)
#         dp = [float('inf')] * (n+1)
#         dp[i] = 0
#         while Q:
#             co, des = heapq.heappop(Q)
#             if visited[des]:
#                 visited[des] = False
#                 for cost, destination in dic[des]:
#                     dp[destination] = min(cost + dp[des], dp[destination])
#                     heapq.heappush(Q, (dp[destination], destination))
#
#
#         ans.append(dp[a] + dp[b] + dp[s])
#         print(ans)
#     print(dp)
#     print(ans)
#     return min(ans)
#



n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]


solution(n, s, a, b, fares)