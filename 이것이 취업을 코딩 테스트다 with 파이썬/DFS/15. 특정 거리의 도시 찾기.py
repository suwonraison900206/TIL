from collections import deque
import sys
sys.stdin = open("15. 특정 거리의 도시 찾기.txt")

N, M, K, X= map(int,input().split())

graph = [[] for _ in range(N + 1)]



for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)


distance = [-1] * (N+1)
distance[X] = 0

q = deque([X])
while q:
    now = q.popleft()

    for next_node in graph[now]:

        if distance[next_node] == -1:

            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True
if check == False:
    print(-1)






#
# road_lst = [list(map(int,input().split())) for __ in range(M)]
#
# visit_lst = [10000002] * (N+1)
#
#
# stack = deque([X])
#
# count = 1
# stack2 = deque()
# while stack:
#     k = stack.popleft()
#     # print(k)
#     for i in range(len(road_lst)):
#         if road_lst[i][0] == k:
#             stack2.append(road_lst[i][1])
#     # print(k)
#     # print(road_lst, stack2)
#
#
#     if len(stack) == 0 and len(stack) == 0:
#         for i in range(len(stack2)):
#             if count < visit_lst[stack2[i]]:
#                 visit_lst[stack2[i]] = count
#
#         stack = stack2
#         stack2 = deque()
#         count += 1
#
#     if len(road_lst) == 0:
#         break
#
# if K not in visit_lst:
#     print(-1)
# else:
#     for i in range(len(visit_lst)):
#         if visit_lst[i] == K:
#             print(i)