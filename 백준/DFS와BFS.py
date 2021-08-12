import sys
from collections import deque
sys.stdin = open('DFS와BFS.txt')

N, M, V = map(int,input().split())
nodes = [list(map(int,input().split())) for __ in range(M)]
node_info = {}
for i in range(1,N+1):
    node_info[i] = []

for node in nodes:

    node_info[node[0]].append(node[1])
    node_info[node[1]].append(node[0])

for key, value in node_info.items():
    node_info[key].sort()

visit_lst = [0] * (N+1)
visit_lst2 = [0] * (N+1)
stack1 = []
print(node_info)
for i in node_info[V]:
    if i not in stack1:
        stack1.append(i)
stack1 = stack1[::-1]
stack2 = deque()
stack2.append(V)
result1 = [V]
result2 = [V]
visit_lst[V] = 1
visit_lst2[V] = 1
print(stack1)
while stack1:
    w = stack1.pop()
    print(w, stack1)
    print(node_info[w])
    if visit_lst[w] == 0:
        visit_lst[w] = 1
        result1.append(w)

    for i in node_info[w]:
        print(i, 'ii')
        if visit_lst[i] == 0:
            visit_lst[i] = 1
            print(i,'sadasdasdasd')
            stack1.append(i)
            result1.append(i)
            break



while stack2:
    q = stack2.popleft()
    for i in node_info[q]:
        if visit_lst2[i] == 0:
            visit_lst2[i] = 1
            stack2.append(i)
            result2.append(i)


for i in result1:
    print(i,end=' ')
print()
for i in result2:
    print(i, end=' ')


