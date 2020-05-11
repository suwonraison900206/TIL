import sys
sys.stdin = open("retire.txt")

def retire(day, count, number):
    global N
    global lst
    global result

    if number >= N-1:
        result.append(count)
        return
    for i in range(number+1, N):
        if day != 0:
            day = day-1
        else:
            retire(lst[i][0]-1, count + lst[i][1], i)
    result.append(count)
N = int(input())
lst = [list(map(int,input().split())) for __ in range(N)]
result = []
lst_2 = []
for i in range(N):
    if i + lst[i][0] > N:
        lst[i][0] = 0
        lst[i][1] = 0


for i in range(N):
    retire(lst[i][0] -1, lst[i][1], i)
print(max(result))