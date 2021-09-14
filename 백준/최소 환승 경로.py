import sys
sys.stdin = open('최소 환승 경로.txt')

N, L = map(int, input().split())
nodes = [list(map(int, input().split())) for __ in range(L)]
start, target = map(int, input().split())
nodes_dict = {}
visit_lst = [0] * (N + 1)

for i in range(len(nodes)):
    node_dict = {}

    for j in nodes[i]:
        if j == -1:
            continue
        node_dict[j] = 1
    nodes_dict[i] = node_dict

stack = []
for key, value in nodes_dict.items():
    if start in nodes_dict[key]:
        for t in nodes_dict[key]:
            visit_lst[t] = 1
            stack.append(t)

visit_lst[start] = 1
stack2 = []
cnt = 0
flag = 0
while stack:

    q = stack.pop()

    for key, value in nodes_dict.items():
        if flag == 1:
            break
        if q in nodes_dict[key]:
            for w in nodes_dict[key]:
                if visit_lst[w] != 1:
                    visit_lst[w] = 1

                if w == target:

                    flag = 1
                stack2.append(w)
    if flag == 1:
        break
    if not stack and stack2:

        stack = stack2[:]
        stack2 = []
        cnt += 1

print(cnt+1)