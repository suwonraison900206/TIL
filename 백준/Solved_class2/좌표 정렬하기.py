N = int(input())
lst = [list(map(int,input().split())) for __ in range(N)]

print(N, lst)

lst.sort(key=lambda x:(x[0],x[1]))

print(lst)

for x,y in lst:

    print(x, y)