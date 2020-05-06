import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("retire.txt")

def retire(a, count, day, map_list, day_2):
    global N
    global lst, lst_2
    global result
    global number


    if a >= 10:
        result.append(count)
        return

N = int(input())
lst = [list(map(int,input().split())) for __ in range(N)]
result = []
lst_2 = []
number = 0
for i in range(N):
    if i + lst[i][0] > N:
        lst[i][0] = 0
        lst[i][1] = 0

for i in range(N):
    retire(i+1, lst[i][1], lst[i][0], lst, i)

print(result)

