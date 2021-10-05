# def dfs(idx):
#
#     for j in edge[idx]:
#         if dfs_visit_lst[j] == 0:
#             dfs_visit_lst[j] = 1
#             print(j, end=' ')
#             dfs(j)
#
#
#
#
# N, M, V = map(int,input().split())
# nodes = [list(map(int,input().split())) for __ in range(M)]
# bfs_visit_lst = [0 for i in range(N+1)]
# dfs_visit_lst = [0 for i in range(N+1)]
# edge = {}
#
# for x, y in nodes:
#     if x not in edge:
#         edge[x] = [y]
#     else:
#         edge[x].append(y)
#     if y not in edge:
#         edge[y] = [x]
#     else:
#         edge[y].append(x)
# print(edge)
#
# bfs_stack = [V]
# dfs_stack = [V]
# bfs_stack2 = []
# dfs_stack2 = []
#
# bfs_visit_lst[V] = 1
# dfs_visit_lst[V] = 1
#
# bfs_result = []
# dfs_result = []
#
# while bfs_stack:
#
#     q = bfs_stack.pop()
#     bfs_result.append(q)
#     for i in edge[q]:
#         if bfs_visit_lst[i] == 0:
#             bfs_stack2.append(i)
#             bfs_visit_lst[i] = 1
#     print(bfs_stack, bfs_stack2, bfs_result)
#     if not bfs_stack and bfs_stack2:
#         bfs_stack2.sort(reverse=True)
#         bfs_stack = bfs_stack2[:]
#         bfs_stack2 = []
#
# print(V, end = ' ')
# for i in edge[V]:
#
#     if dfs_visit_lst[i] == 0:
#         dfs_visit_lst[i] = 1
#         print(i, end=' ')
#
#         dfs(i)
#
#
# print()
# for i, v in enumerate(bfs_result):
#     print(v, end=' ')


# 최종제출
from collections import deque
n, m, v = map(int, input().split())
input_lst = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: (x[0], x[1]))
edge_lst = [[] for _ in range(n + 1)]
for v1, v2 in input_lst:
    edge_lst[v1].append(v2)
    edge_lst[v2].append(v1)
visited = [0] * (n + 1)
dfs_lst = []

print(edge_lst)
def dfs(v, dfs_lst):
    # 1. 방문한 노드인지 확인
    if visited[v] == 0:
        dfs_lst.append(v)
        # 방문처리
        visited[v] = 1
        # 2. 인접한 노드 순회
        for v2 in sorted(edge_lst[v]):
            dfs(v2, dfs_lst)
        return dfs_lst
print(*dfs(v, dfs_lst))


visited = [0] * (n + 1)
q = deque()
# 첫 노드 큐삽입 & 방문처리
q.append(v)
visited[v] = 1
bfs_lst = [v]
while 1:
    for v2 in sorted(edge_lst[v]):
        if visited[v2] == 0:
            q.append(v2)
            bfs_lst.append(v2)
            visited[v2] = 1
    if len(q) == 0:
        break
    v = q.popleft()
print(*bfs_lst)
