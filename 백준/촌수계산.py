import sys
sys.stdin = open('촌수계산.txt')

n = int(input())
target = list(map(int,input().split()))
m = int(input())
nodes = [list(map(int,input().split())) for __ in range(m)]
family = {}
visit_lst = [0] * (n+1)
for node in nodes:

    if node[0] not in family:
        family[node[0]] = [node[1]]
    else:
        family[node[0]].append(node[1])
    if node[1] not in family:
        family[node[1]] = [node[0]]
    else:
        family[node[1]].append(node[0])

print(visit_lst)
print(family)

stack = [target[0]]
stack2 = []
visit_lst[target[0]] = 1
print(stack)
cnt = 1
flag= 0
while stack:

    q = stack.pop()
    if q == target[1]:
        flag= 1
        break
    for i in family[q]:
        if visit_lst[i] == 0:
            visit_lst[i] = 1
            stack2.append(i)

    if not stack and stack2:
        stack = stack2[:]
        stack2 = []
        cnt +=1

if flag == 0:
    print(-1)
else:
    print(cnt-1)

