N = int(input())
N_lst = [list(map(int,input().split())) for __ in range(N)]

N_lst.sort(key=lambda x:(x[1], x[0], x[1]-x[0]))

result = 0
cnt = 0
print(N_lst)
for start, end in N_lst:

    if start >= result:
        result = end
        cnt +=1

print(cnt)