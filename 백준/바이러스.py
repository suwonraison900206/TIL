import sys
sys.stdin = open('바이러스.txt')

computers = int(input())
network = int(input())
nodes = [list(map(int,input().split())) for __ in range(network)]
computer_lst = [0] * (computers+1)
node_info = {}

for node in nodes:
    if node[0] not in node_info:
        node_info[node[0]] = [node[1]]
    else:
        node_info[node[0]].append(node[1])

    if node[1] not in node_info:
        node_info[node[1]] = [node[0]]
    else:
        node_info[node[1]].append(node[0])

stack = [1]
computer_lst[1] = 1

while stack:
    q = stack.pop()

    for i in node_info[q]:
        if computer_lst[i] == 0:
            stack.append(i)
            computer_lst[i] = 1


print(sum(computer_lst) -1)