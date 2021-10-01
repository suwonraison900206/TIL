N, K = map(int,input().split())

lst = [i for i in range(1, N+1)]
cnt = 1
flag = 0
W = len(lst)
result = []
while lst:

    if cnt == K:
        result.append(lst.pop(flag))

        W -=1
        cnt = 1

    else:
        cnt +=1
        flag += 1
    if flag == W :
        flag = 0

q = '<'

for i,v in enumerate(result):
    if i != len(result)-1:
        q = q + str(v) +', '
    else:
        q = q + str(v) + '>'
print(q)