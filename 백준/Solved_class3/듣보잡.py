N, M = map(int,input().split())
N_lst = [input() for __ in range(N)]
M_lst = [input() for __ in range(M)]
target = N_lst + M_lst
result = []
a = {}
b = {}
for i in N_lst:
    a[i] = 1
for i in M_lst:
    b[i] = 1
for t in target:

    if t in a and t in b and t not in result:
        result.append(t)

result.sort()
print(len(result))
for r in result:
    print(r)