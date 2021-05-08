from itertools import permutations
import sys
sys.stdin = open('연산자 끼워넣기.txt')

N = int(input())
num_lst = list(map(int,input().split()))
yunsan = list(map(int,input().split()))
lst = []
for i in range(len(yunsan)):
    for j in range(yunsan[i]):
        if i == 0:
            lst.append('+')
        elif i == 1:
            lst.append('-')
        elif i == 2:
            lst.append('*')
        elif i == 3:
            lst.append('/')

result_lst= []
for i in permutations(lst,N-1):
    cnt = 0
    for j in range(0, len(num_lst)-1):
        if j == 0:
            if i[j] == '+':
                cnt = (num_lst[j] + num_lst[j+1])
            elif i[j] == '-':
                cnt = (num_lst[j] - num_lst[j + 1])
            elif i[j] == '*':
                cnt = (num_lst[j] * num_lst[j + 1])
            elif i[j] == '/':
                cnt = int((num_lst[j] / num_lst[j + 1]))
        else:
            if i[j] == '+':
                cnt += num_lst[j+1]
            elif i[j] == '-':
                cnt -= num_lst[j + 1]
            elif i[j] == '*':
                cnt = cnt * num_lst[j + 1]
            elif i[j] == '/':
                cnt = int(cnt / num_lst[j + 1])

    result_lst.append(cnt)

print(max(result_lst))
print(min(result_lst))
