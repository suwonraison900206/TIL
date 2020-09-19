import sys
sys.stdin = open("연산자 끼워넣기.txt")
from itertools import permutations


N = int(input())
number_lst = list(map(int,input().split()))
lst = list(map(int,input().split()))
cnt_lst = []
for i in range(len(lst)):
    for j in range(lst[i]):
        cnt_lst.append([i, j])
k = list(permutations(cnt_lst,len(cnt_lst)))
stack = []

for i in range(len(k)):
    cnt = number_lst[0]
    for q in range(N-1):
        if k[i][q][0] == 0:
            cnt = cnt + number_lst[q+1]
        elif k[i][q][0] == 1:
            cnt = cnt - number_lst[q+1]
        elif k[i][q][0] == 2:
            cnt = cnt * number_lst[q+1]
        elif k[i][q][0] == 3:
            if cnt < 0:
                cnt = -(-(cnt) // number_lst[q+1])
            else:
                cnt = cnt // number_lst[q + 1]
    if -1000000000 <= cnt < 1000000000:
        stack.append(cnt)


print(max(stack))
print(min(stack))


