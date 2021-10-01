N = int(input())
lst = [list(map(int,input().split())) for __ in range(N)]

lst.sort(key=lambda x:(x[1],x[0]))

for x,y in lst:

    print(x, y)