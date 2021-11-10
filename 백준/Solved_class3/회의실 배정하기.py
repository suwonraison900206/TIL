N = int(input())
N_lst = [list(map(int,input().split())) for __ in range(N)]
N_lst.sort(key=lambda x: (x[1], x[0]))
result = 0
cnt = 0

for start, end in N_lst:
    if start >= result:
        result = end
        cnt +=1

print(cnt)


a = int(input())
b = [list(map(int, input().split())) for _ in range(a)]
b.sort(key=lambda x: (x[1], x[0]))
time = 0
count = 0
if len(b) == 1:
    print(1)
else:
    def func():
        for idx, i in enumerate(b):
            if(i[0] >= time):
                if(i[0] == i[1]):
                    del b[idx]
                return i[1]
    while b[len(b)-1][0] >= time:
        count = count + 1
        time = func()
    print(count)